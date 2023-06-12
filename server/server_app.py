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
data = {}
try:
    while True:
        client, address = sock.accept()
        print(f"Got connection from: {address}")
        print('Press Ctrl+c to exit.')
         #TODO: handle client.send only when data changes. 
        while True:
            #Check connection to iRacing
            iracing.check_iracing()
            if iracing.ir_connected:
                data_1 = iracing.get_data()
                if data != data_1:
                    data = data_1
                    data_str = json.dumps(data)
                    try:
                        client.send(data_str.encode())
                        print('sending data to client') 
                    except Exception as err:
                        print(f"Error: {err}")
                        client, address = sock.accept()
                        print(f"Got connection from: {address}")
            time.sleep(0.05) 

except KeyboardInterrupt:
    #ctrl+c to exit
    print('Server terminated.')
    pass

            

    