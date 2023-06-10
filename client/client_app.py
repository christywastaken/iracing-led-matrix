import socket
from matrix_model import LEDMatrixDisplay

sock = socket.socket()
PORT = 1234
PC_IP = '10.83.1.178'
sock.connect((PC_IP, PORT))

matrix = LEDMatrixDisplay()

try:
    while True:
        data = sock.recv(1024)
        matrix.process_data(data)
        print(data)
except KeyboardInterrupt:
    print('Client terminated.')

