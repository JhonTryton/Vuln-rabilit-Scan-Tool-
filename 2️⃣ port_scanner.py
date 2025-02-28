import nmap

def scan_ports(ip):
    scanner = nmap.PortScanner()
    scanner.scan(ip, arguments="-sV")  # Détecte les versions des services
    open_ports = {}
    
    for proto in scanner[ip].all_protocols():
        ports = scanner[ip][proto]
        for port, data in ports.items():
            open_ports[port] = {"service": data.get("name", "unknown"), "version": data.get("version", "unknown")}
    
    return open_ports
  
