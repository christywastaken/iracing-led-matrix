import irsdk


class IRacing():
    def __init__(self):
        self.ir = irsdk.IRSDK()
        self.ir_connected = False
        self.last_car_setup_tick = -1
        self.last_data = {}
        self.last_data_tick = 0


    def check_iracing(self):
        if self.ir_connected and not (self.ir.is_initialized and self.ir.is_connected):
            #Reset variables and and shutdown self.ir library (clear all internal variables)
            self.ir_connected = False
            self.last_car_setup_tick = -1
            self.last_data_tick = 0
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
    

    def get_bb(self):
        if self.ir['dcBrakeBias']:
            return round(self.ir['dcBrakeBias'],1)
        else:
            return 0
    

    def get_ABS(self):
        try: 
            return self.ir['BrakeABSactive']
        except:
            return 0


    def get_data(self):
        gear = self.get_gear()
        flags = self.get_flags()
        abs_active = self.get_ABS()
        brake_bias = self.get_bb()
        return {'gear': gear, 
                'flags': flags, 
                'abs_active': abs_active, 
                "brake_bias": brake_bias}
        

    def check_new_data(self):
        data = self.get_data()
        if self.last_data != data:
            self.last_data = data
            self.last_data_tick += 1
            return True
        else:
            return False
    



