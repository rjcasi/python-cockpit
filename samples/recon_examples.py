from src.recon import dir_bruteforce, subdomain_scanner, port_scan

# Directory brute force
dirs = dir_bruteforce.scan("http://example.com", wordlist="common.txt")
print("Directories found:", dirs)

# Subdomain scan
subs = subdomain_scanner.find("example.com")
print("Subdomains:", subs)

# Port scan
ports = port_scan.scan("example.com", ports=[80, 443, 22])
print("Open ports:", ports)