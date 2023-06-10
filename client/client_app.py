import socket
from matrix_model import process_data

sock = socket.socket()

PORT = 12345

PC_IP = '10.83.1.178'

sock.connect((PC_IP, PORT))


while True:
    data = sock.recv(1024)
    process_data(data)
    
    
