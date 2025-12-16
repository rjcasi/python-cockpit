import socket

def scan_ports(target_host, ports):
    print(f"Scanning {target_host}...")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((target_host, port))
            if result == 0:
                print(f"Port {port}: OPEN")
            else:
                print(f"Port {port}: CLOSED")
            sock.close()
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

if __name__ == "__main__":
    # Example: scan common ports on localhost
    common_ports = [22, 80, 443, 3306]
    scan_ports("127.0.0.1", common_ports)