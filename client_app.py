import socket

sock = socket.socket()

port = 12345

mac_ip = '10.83.1.239'

sock.connect((mac_ip, port))

def process_data(data):
    print(f'Received data: {data}')

while True:
    data = sock.recv(1024)
    process_data(data)
    #TODO: Logic for data and led functions.
    