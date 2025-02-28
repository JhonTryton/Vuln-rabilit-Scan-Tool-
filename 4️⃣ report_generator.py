import csv

def save_report(data, filename="vulnerability_report.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["IP", "Port", "Service", "Version", "Vulnérabilités"])
        for ip, ports in data.items():
            for port, details in ports.items():
                writer.writerow([ip, port, details['service'], details['version'], ", ".join(details['vulns'])])
              
