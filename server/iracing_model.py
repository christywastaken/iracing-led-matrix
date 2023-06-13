import irsdk


class IRacing():
    def __init__(self):
        self.ir = irsdk.IRSDK()
        self.ir_connected = False
        self.last_car_setup_tick = -1
       

    def check_iracing(self):
        if self.ir_connected and not (self.ir.is_initialized and self.ir.is_connected):
            #Reset variables and and shutdown self.ir library (clear all internal variables)
            self.ir_connected = False
            self.last_car_setup_tick = -1
            self.ir.shutdown()
            print('irsdk disconnected')
        elif not self.ir_connected and self.ir.startup() and self.ir.is_initialized and self.ir.is_connected:
            self.ir_connected = True
            print('irsdk connected')

    def get_gear(self):
        try:
            return self.ir['Gear']
        except: 
            return 0
        
    def get_flags(self):
        try: 
            return self.ir['SessionFlags']
        except:
            return None

    def get_data(self):
        gear = self.get_gear()
        flags = self.get_flags()
        return {'gear': gear, 'flags': flags}
    



