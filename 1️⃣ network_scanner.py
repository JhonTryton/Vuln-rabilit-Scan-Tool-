import nmap

def scan_network(network):
    scanner = nmap.PortScanner()
    scanner.scan(hosts=network, arguments="-sn")  # Scan sans port
    active_hosts = [host for host in scanner.all_hosts()]
    return active_hosts
  
