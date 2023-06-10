import socket
from matrix_model import process_data

sock = socket.socket()

PORT = 12345

PC_IP = '10.83.1.178'

sock.connect((PC_IP, PORT))

try:
    while True:
        data = sock.recv(1024)
        process_data(data)
        print(data)
except KeyboardInterrupt:
    print('Client terminated.')

