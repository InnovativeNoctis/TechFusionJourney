# Port Scanner (TechFusionJourney)

A simple, lightweight IPv4 port scanner implemented in pure Python. This scanner performs TCP and UDP probes using the Python standard library and is intended for learning, experimentation, and small lab use. It is part of the **TechFusionJourney** repository.

---

## Features

* TCP connect-based probing (determines open/closed by attempting a TCP `connect()`).
* UDP probing (sends an empty UDP datagram and checks for a response — note the inherent ambiguity in UDP scanning).
* Uses a CSV-based service/port database (`service-names-port-numbers.csv`) to map port numbers to service names and descriptions.
* Batched, multithreaded scanning with configurable worker counts and timeouts.
* Progress/console reporting and printing of discovered open ports in real time.
* No external dependencies — pure Python standard library.

---

## Files in this tool

* `main.py` — CLI entry point and batch/worker orchestration.
* `ip_manager.py` — command-line parsing and IP/subnet expansion.
* `scanner.py` — low-level TCP/UDP probe functions.
* `port_database.py` — CSV loader that expands port ranges and returns port/service records.
* `multithreader.py` — small helper for running work across a thread pool.
* `service-names-port-numbers.csv` — **Required** IANA CSV file (not included); see below.

---

## Quick start

1. Clone your repository (or copy the code into a project directory):

```bash
git clone https://github.com/InnovativeNoctis/TechFusionJourney.git
cd TechFusionJourney
```

2. Ensure the IANA CSV file (`service-names-port-numbers.csv`) is in the project root (or the same folder as `port_database.py`). You can download the official CSV from IANA (Service Name and Transport Protocol Port Number Registry).

3. Run the scanner (examples below). The scanner uses only the standard library so no `pip` dependencies are required.

---

## Usage

```
python main.py <target-ip-or-subnet> [options]
```

### Positional

* `ip` — target IP or subnet (e.g. `192.168.1.1` or `192.168.1.0/24`). Use `localhost` to scan `127.0.0.1`.

### Options

* `-sT` — scan TCP (default)
* `-sU` — scan UDP
* `-p <ports...>` — ports to scan (e.g. `-p 80 443`), or `all` to use every port from the CSV. Default: `common`
* `--workers` — max concurrent worker threads (default: `100`)
* `--timeout` — socket timeout in seconds (default: `0.8`)
* `--batch` — batch size for tasks to limit memory/spike usage (default: `5000`)

### Examples

Scan common ports (default) on a single host (TCP):

```bash
python main.py 192.168.1.10
```

Scan custom ports on a host:

```bash
python main.py 192.168.1.10 -p 22 80 443 --workers 200 --timeout 1.0
```

Scan all ports listed in the CSV for a /24 network (be careful — this is noisy and slow):

```bash
python main.py 192.168.1.0/24 -p all --workers 300 --batch 2000
```

Scan UDP on localhost:

```bash
python main.py localhost -sU -p 53 123
```

---

## Output

* The scanner prints discovered open ports in a concise format:

```
[+] 192.168.1.10:80 : http :: Open ---> Hypertext Transfer Protocol
```

* Progress is shown as an updating line: `Scanning tasks: 123/900 (13.7%)`.

---

## Important notes & limitations

* **IPv4 only**: The current implementation uses `AF_INET` sockets. IPv6 is not supported yet.
* **UDP ambiguity**: Many UDP services do not reply to empty datagrams — lack of response is ambiguous and reported as `Open|Filtered (no response)`.
* **Permissions**: The scanner uses ordinary sockets and typically doesn't require root privileges for probing remote ports, but some environments or system firewalls may affect results.
* **CSV file**: `port_database.py` expects the IANA CSV file (`service-names-port-numbers.csv`) in the working directory. You can obtain it from IANA’s registry.
* **Ethics & legality**: Do **not** scan IP ranges/networks you do not own or do not have explicit permission to test. Unauthorized scanning may be illegal or violate terms of service.

---

## Suggestions & TODO

* Add IPv6 support.
* Option to output results in structured formats (JSON/CSV) or write to a file.
* Rate-limiting / adaptive timeouts for large networks.
* More robust error handling and retries for transient network errors.
* Add unit tests and CI (e.g. GitHub Actions) for core components.

---

## Contributing

Contributions, bug reports and improvements are welcome. Please open an issue or submit a pull request against the `TechFusionJourney` repository.

When contributing:

* Keep changes focused and documented.
* Add tests for new features if applicable.
* Respect the ethical scanning notice above.

---

## License

Suggested: **MIT License** — simple, permissive, and common for small tools. If you prefer another license (GPL, Apache), change as needed.

---

## Contact

* GitHub: [InnovativeNoctis](https://github.com/InnovativeNoctis)