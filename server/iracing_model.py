import irsdk
import time

ir = irsdk.IRSDK()


class IRacing():

    ir_connected = False
    last_car_setup_tick = -1

    def check_iracing(self):
        if self.ir_connected and not (ir.is_initialized and ir.is_connected):
            #Reset variables and and shutdown ir library (clear all internal variables)
            self.ir_connected = False
            self.last_car_setup_tick = -1
            ir.shutdown()
            print('irsdk disconnected')
        elif not self.ir_connected and ir.startup() and ir.is_initialized and ir.is_connected:
            self.ir_connected = True
            print('irsdk connected')


    def get_gear(self):
        try:
            return ir['Gear']
        except: 
            return 0


    def get_data(self):
        gear = self.get_gear()
        return {'gear': gear}
    



