import irsdk
import time
print('we are here')
ir = irsdk.IRSDK()
ir.startup()

def get_gear():
    return ir['CarIdxGear'][0]

