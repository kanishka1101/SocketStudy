import socket

HOST = '127.0.0.1'
PORT = 8080

def start_client():
    # Create socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to server
    client.connect((HOST, PORT))

    # Send message
    client.sendall("Hello from Client".encode())
    print("Message sent to server")

    # Receive response
    data = client.recv(1024).decode()
    print("Server:", data)

    # Close connection
    client.close()

if __name__ == "__main__":
    start_client()
