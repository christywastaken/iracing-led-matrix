import socket
import time
sock = socket.socket()

port = 12345

sock.bind(('', port))

sock.listen(1)
print('listening for client')


while True:
    
    client, address = sock.accept()
    print(f"Got connection from: {address}")
    
    time.sleep(2)
    while True:
        client.send(input('Enter some data: ').encode())