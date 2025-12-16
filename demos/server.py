import socket

def run_demo():
    host = "127.0.0.1"  # localhost
    port = 65432        # arbitrary non-privileged port

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")
        conn, addr = s.accept()
        with conn:
            print("Connected by", addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print("Received:", data.decode())
                conn.sendall(b"Hello from server")