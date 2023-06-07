import socket
from matrix_model import process_data

sock = socket.socket()

PORT = 12345

MAC_IP = '10.83.1.239'

sock.connect((MAC_IP, PORT))


while True:
    data = sock.recv(1024)
    process_data(data)
    
    