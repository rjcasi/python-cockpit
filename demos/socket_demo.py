import socket
import threading

def run_server(host="127.0.0.1", port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"[SERVER] Listening on {host}:{port}")
        conn, addr = s.accept()
        with conn:
            print(f"[SERVER] Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print("[SERVER] Received:", data.decode())
                conn.sendall(b"Hello from server")

def run_client(host="127.0.0.1", port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b"Hello from client")
        data = s.recv(1024)
        print("[CLIENT] Received:", data.decode())

def run_demo():
    """
    Standard entry point for the socket demo.
    Spins up a server and client in separate threads.
    """
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()

    # Give the server a moment to start
    import time; time.sleep(1)

    run_client()
    print("Socket demo finished.")