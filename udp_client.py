import socket

# Define the server address and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send data to the server
message = "Hello, UDP Server!"
client_socket.sendto(message.encode(), (SERVER_HOST, SERVER_PORT))

# Receive data from the server
data, _ = client_socket.recvfrom(1024)
print(f"[*] Received from server: {data.decode()}")

# Close the socket
client_socket.close()