# import socket

# # Define the server address and port
# SERVER_HOST = '127.0.0.1'
# SERVER_PORT = 12345

# # Create a TCP socket
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Connect to the server
# client_socket.connect((SERVER_HOST, SERVER_PORT))

# # Send data to the server
# message = "Hello, TCP Server!"
# client_socket.sendall(message.encode())

# # Receive data from the server
# data = client_socket.recv(1024)
# print(f"[*] Received: {data.decode()}")

# # Close the connection
# client_socket.close()