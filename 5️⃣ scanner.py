from network_scanner import scan_network
from port_scanner import scan_ports
from vulnerability_checker import check_vulnerabilities
from report_generator import save_report

# Définir la plage IP
network = "192.168.1.0/24"  # À modifier selon votre réseau
machines = scan_network(network)

scan_results = {}

for machine in machines:
    print(f"Scanning {machine}...")
    services = scan_ports(machine)
    
    for port, details in services.items():
        vulns = check_vulnerabilities(details['service'], details['version'])
        services[port]["vulns"] = [v["id"] for v in vulns] if vulns else []
    
    scan_results[machine] = services

# Sauvegarde du rapport
save_report(scan_results)
print("Rapport généré : vulnerability_report.csv")
