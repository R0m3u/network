
import socket
import os

HOST = '192.168.0.9'  # Bind to all interfaces
PORT = 12345      # Port to listen on

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Server listening on {HOST}:{PORT}")

conn, addr = server_socket.accept()
print(f"Connection established with {addr}")


data = conn.recv(1024).decode()
os.system(data)
print(f"Received: {data}")

msg = str(input(">"))
conn.sendall(msg.encode())
conn.close()
server_socket.close()
