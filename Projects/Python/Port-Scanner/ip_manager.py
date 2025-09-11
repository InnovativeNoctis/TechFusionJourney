import ipaddress
import argparse

def manage(ip_str="localhost"):
    if ip_str == "localhost":
        return [ipaddress.ip_address("127.0.0.1")]

    try:
        if "/" in ip_str:
            return list(ipaddress.ip_network(ip_str, strict=False).hosts())
        else:
            return [ipaddress.ip_address(ip_str)]
    except ValueError:
        return False

def get():
    parser = argparse.ArgumentParser(description="Port scanner tool")
    parser.add_argument("ip", help="Target ip or subnet (e.g. 192.168.1.1 or 192.168.1.0/24)")

    parser.add_argument("-sT", dest="protocol", action="store_const", const="tcp",
                        help="Scan TCP protocol (default)")
    parser.add_argument("-sU", dest="protocol", action="store_const", const="udp",
                        help="Scan UDP protocol")

    parser.add_argument("-p", dest="ports", nargs="+",
                        help="Port(s) to scan, e.g. '80 443' or 'all' (default: common)")

    parser.add_argument("--workers", type=int, default=100,
                        help="Max concurrent worker threads (default: 100)")
    parser.add_argument("--timeout", type=float, default=0.8,
                        help="Socket timeout in seconds (default: 0.8)")
    parser.add_argument("--batch", type=int, default=5000,
                        help="Batch size for tasks (default: 5000). Use smaller to reduce resource spikes.")

    parser.set_defaults(protocol="tcp", ports=["common"], workers=100, timeout=0.8, batch=5000)
    args = parser.parse_args()
    return vars(args)
