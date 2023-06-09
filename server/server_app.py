import socket
import time
import json
from iracing_model import IRacing

sock = socket.socket()
port = 12345
sock.bind(('', port))
sock.listen(1)
print('listening for client')

iracing = IRacing()

try:
    while True:
        client, address = sock.accept()
        print(f"Got connection from: {address}")
        print('Press Ctrl+c to exit.')
        
        while True:
            #Check connection to iRacing
            iracing.check_iracing()
            if iracing.ir_connected:
                data = iracing.get_data()
                data_str = json.dumps(data)
                client.send(data.encode()) 
            time.sleep(0.05) 

except KeyboardInterrupt:
    #ctrl+c tp exit
    print('Server terminated.')
    pass

            

    