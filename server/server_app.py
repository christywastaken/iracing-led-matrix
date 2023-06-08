import socket
import time
from iracing_test import get_gear

sock = socket.socket()
port = 12345
sock.bind(('', port))
sock.listen(1)
print('listening for client')


while True:
    
    client, address = sock.accept()
    print(f"Got connection from: {address}")
    
    while True:
        gear_str1 = str(get_gear())
        time.sleep(0.05)
        gear_str2 = str(get_gear())
        if gear_str1 != gear_str2:
            client.send(gear_str2.encode())

    