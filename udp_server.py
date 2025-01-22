import socket

# Define the server address and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the address and port
server_socket.bind((SERVER_HOST, SERVER_PORT))

print(f"[*] Listening on {SERVER_HOST}:{SERVER_PORT}")

# Receive data from the client
data, client_address = server_socket.recvfrom(1024)
print(f"[*] Received from {client_address[0]}:{client_address[1]}: {data.decode()}")

# Echo back the received data
server_socket.sendto(data, client_address)

# Close the socket
server_socket.close()
