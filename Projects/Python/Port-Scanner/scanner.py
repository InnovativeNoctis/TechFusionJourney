import socket

def default_scan(ip, port, description="", service="", protocol="tcp", timeout=0.8):
   
    ip_str = str(ip)
    port = int(port)
    result = {
        "ip": ip_str,
        "port": port,
        "service": service,
        "protocol": protocol,
        "status": "Closed",
        "description": description
    }

    proto = protocol.lower()
    try:
        if proto == "tcp":
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(timeout)
            try:
                client.connect((ip_str, port))
                result["status"] = "Open"
            except (socket.timeout, ConnectionRefusedError, OSError):
                result["status"] = "Closed"
            finally:
                client.close()
            return result

        elif proto == "udp":
            client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            client.settimeout(timeout)
            try:
                client.sendto(b"", (ip_str, port))
                try:
                    client.recvfrom(1024)
                    result["status"] = "Open"
                except socket.timeout:
                    result["status"] = "Open|Filtered (no response)"
            except OSError:
                result["status"] = "Closed"
            finally:
                client.close()
            return result

        else:
            result["status"] = "Invalid protocol"
            return result

    except Exception as exc:
        result["status"] = "Closed"
        result["description"] = f"scan error: {exc}"
        return result
