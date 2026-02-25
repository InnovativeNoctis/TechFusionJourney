import argparse
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

# -----------------------------
# Arguments
# -----------------------------
parser = argparse.ArgumentParser(description="Fast Threaded Port Scanner")
parser.add_argument("ip", type=str, help="Target IP address")
parser.add_argument(
    "-p", "--port",
    type=str,
    default="1-1024",
    help="Port(s) to scan (e.g., 80, 20-25, or 1-1024)"
)
parser.add_argument(
    "-t", "--timeout",
    type=float,
    default=2.0,
    help="Connection timeout in seconds"
)
parser.add_argument(
    "-w", "--workers",
    type=int,
    default=100,
    help="Number of concurrent threads"
)

args = parser.parse_args()


# -----------------------------
# Port Parsing
# -----------------------------
def parse_ports(port_input: str):
    """Convert a port string into a list of integers."""
    if "-" in port_input:
        start, end = port_input.split("-", 1)
        return list(range(int(start), int(end) + 1))
    elif "," in port_input:
        return [int(p.strip()) for p in port_input.split(",")]
    else:
        return [int(port_input)]


# -----------------------------
# Single Port Scan
# -----------------------------
def scan_port(ip: str, port: int, timeout: float):
    """Scan a single port and return its status."""
    client = None
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(timeout)
        client.connect((ip, port))
        return port, "Open"

    except ConnectionRefusedError:
        return port, "Closed"
    except socket.timeout:
        return port, "Filtered"
    except socket.gaierror:
        return port, "Hostname could not be resolved"
    except OverflowError:
        return port, "Port out of range"
    except Exception as e:
        return port, f"Error: {e}"
    finally:
        if client:
            client.close()


# -----------------------------
# Threaded Scan
# -----------------------------
def threaded_scan(ip, ports, timeout, workers):
    results = {}

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [
            executor.submit(scan_port, ip, port, timeout)
            for port in ports
        ]

        for future in as_completed(futures):
            port, status = future.result()
            results[port] = status
            print(f"Port {port}: {status}")

    return results


# -----------------------------
# Entry Point
# -----------------------------
if __name__ == "__main__":
    try:
        ports = parse_ports(args.port)
        threaded_scan(args.ip, ports, args.timeout, args.workers)

    except KeyboardInterrupt:
        print("\nScan interrupted by user.")