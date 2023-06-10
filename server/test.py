import irsdk
import time

ir = irsdk.IRSDK()

ir_connected = False
last_car_setup_tick = -1

def check_iracing():
    global ir_connected, last_car_setup_tick
    if ir_connected and not (ir.is_initialized and ir.is_connected):
        #Reset variables and and shutdown ir library (clear all internal variables)
        ir_connected = False
        last_car_setup_tick = -1
        ir.shutdown()
        print('irsdk disconnected')
    elif not ir_connected and ir.startup() and ir.is_initialized and ir.is_connected:
        ir_connected = True
        print('irsdk connected')


def get_gear():
    try:
        return ir['Gear']
    except Exception as err:
        print(f'Error: {err}') 
        return 0


def get_data():
    gear = get_gear()
    return {'gear': gear}

check_iracing()
print(get_gear())