import socket

HOST = '127.0.0.1'   # Localhost
PORT = 8080

def start_server():
    # Create socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind socket
    server.bind((HOST, PORT))

    # Listen for connections
    server.listen(1)
    print(f"Server listening on {HOST}:{PORT}...")

    # Accept connection
    conn, addr = server.accept()
    print(f"Connected by {addr}")

    # Receive data
    data = conn.recv(1024).decode()
    print("Client:", data)

    # Send response
    conn.sendall("Hello from Server".encode())

    # Close connection
    conn.close()
    server.close()

if __name__ == "__main__":
    start_server()
