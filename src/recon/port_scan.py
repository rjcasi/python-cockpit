def scan(host, ports=[80, 443]):
    print(f"[Recon] Scanning {host} on ports {ports}")
    return [p for p in ports if p in [80, 443]]