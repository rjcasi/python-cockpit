# Combine recon scans
from src.recon import subdomain_scanner, port_scan

subs = subdomain_scanner.find("example.com")
for sub in subs:
    open_ports = port_scan.scan(sub, ports=[80, 443])
    print(f"{sub} -> {open_ports}")