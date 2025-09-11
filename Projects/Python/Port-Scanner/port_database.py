import csv 

def database(usr_protocol="tcp"):
    def process_row(row):
        port = row["Port Number"]
        service = row["Service Name"]
        description = row["Description"]

        if not port or not service:
            return []

        if "-" in port:
            start, end = map(int, port.split("-"))
            return [{"Port": p, "Service": service, "Description": description} 
                    for p in range(start, end+1)]
        else:
            return [{"Port": int(port), "Service": service, "Description": description}]

    with open("service-names-port-numbers.csv", newline="", encoding="utf-8") as db:
        reader = csv.DictReader(db)
        results = []

        for row in reader:
            protocol = row["Transport Protocol"].lower()

            if usr_protocol.lower() in ("tcp", "udp") and protocol != usr_protocol.lower():
                continue

            results.extend(process_row(row))

        return results