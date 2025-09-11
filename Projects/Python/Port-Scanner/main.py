from port_database import database
from scanner import default_scan
import ip_manager
from concurrent.futures import ThreadPoolExecutor, as_completed
import sys
import time
import threading

COMMON_PORTS = [22, 80, 443, 8080, 53, 21, 25, 110, 995]

print_lock = threading.Lock()

def run_scan(ip_addr, usr_ports, ip_prtcl, workers, timeout, batch_size):
    all_tasks = [
        (str(ip), int(port["Port"]), port.get("Description", ""), port.get("Service", ""), ip_prtcl)
        for ip in ip_addr
        for port in usr_ports
    ]

    total_tasks = len(all_tasks)
    print(f"DEBUG: IPs={len(ip_addr)}, ports={len(usr_ports)}, total tasks={total_tasks}", file=sys.stderr)

    if total_tasks == 0:
        print("No tasks to scan. Exiting.")
        return

    scan_results = []
    completed = 0
    last_update = 0.0
    THROTTLE = 0.1 

    for i in range(0, total_tasks, batch_size):
        batch = all_tasks[i:i + batch_size]
        batch_workers = min(workers, len(batch))
        futures = {}

        with ThreadPoolExecutor(max_workers=batch_workers) as executor:
            for (ip, port, desc, svc, proto) in batch:
                futures[executor.submit(default_scan, ip, port, desc, svc, proto, timeout)] = (ip, port)

            try:
                for future in as_completed(futures):
                    try:
                        res = future.result()
                    except Exception as exc:
                        ip, port = futures.get(future, (None, None))
                        res = {
                            "ip": ip,
                            "port": port,
                            "service": None,
                            "protocol": ip_prtcl,
                            "status": "Closed",
                            "description": f"scan error: {exc}"
                        }

                    scan_results.append(res)
                    completed += 1

                    if res.get("status") in ("Open", "Open|Filtered (no response)"):
                        with print_lock:
                            print(f"[+] {res.get('ip')}:{res.get('port')} : {res.get('service')} "
                                  f":: {res.get('status')} ---> {res.get('description')}")

                    now = time.time()
                    if (now - last_update) >= THROTTLE or completed == total_tasks:
                        pct = (completed / total_tasks) * 100.0
                        print(f"\rScanning tasks: {completed}/{total_tasks} ({pct:.1f}%)", end="", flush=True)
                        last_update = now

            except KeyboardInterrupt:
                print("\nScan interrupted by user. Cancelling remaining tasks...", file=sys.stderr)
                for f in futures:
                    f.cancel()
                return

    print()

    scan_results.sort(key=lambda r: (int(r.get("port") or 0), str(r.get("ip") or "")))

def main():
    command = ip_manager.get()

    ip_addr = ip_manager.manage(command["ip"])
    if not ip_addr:
        print("Invalid IP address or subnet. Exiting.")
        return

    ip_prtcl = command["protocol"].lower()
    db_ports = database(ip_prtcl)

    ports_arg = command.get("ports", ["common"])

    if any(str(p).lower() == "all" for p in ports_arg):
        usr_ports = db_ports
    elif ports_arg == ["common"]:
        usr_ports = [p for p in db_ports if int(p["Port"]) in COMMON_PORTS]
    else:
        try:
            user_ports_int = {int(p) for p in ports_arg}
        except ValueError:
            print("Invalid ports specified. Use integers or 'all'. Exiting.")
            return
        usr_ports = [p for p in db_ports if int(p["Port"]) in user_ports_int]

    if not usr_ports:
        print("No valid ports found to scan. Exiting.")
        return

    workers = int(command.get("workers", 100))
    timeout = float(command.get("timeout", 0.8))
    batch_size = int(command.get("batch", 5000))

    run_scan(ip_addr, usr_ports, ip_prtcl, workers, timeout, batch_size)

if __name__ == "__main__":
    main()
