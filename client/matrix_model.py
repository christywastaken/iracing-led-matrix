from rgbmatrix import RGBMatrix, RGBMatrixOptions 
import ast
import json

class LEDMatrixDisplay:
    #TODO: workout more efficient way to display pixels.
    #TODO: fix the conflict between flags and gears
    def __init__(self):
        options = RGBMatrixOptions()
        options.rows = 32
        options.cols = 64
        options.chain_length = 1 
        options.parallel = 1
        options.disable_hardware_pulsing = 1
        options.brightness = 50
        options.hardware_mapping = 'adafruit-hat'

        self.matrix = RGBMatrix(options=options)

        self.gears_coords_list = []
        self.flag_coords_dict = {}
        self.gear = None
        self.flag = None

        with open('../client/gears_coords.txt', 'r') as f:
            for line in f:
                line.strip()
                data_list = ast.literal_eval(line)
                self.gears_coords_list.append(data_list)

        with open('../client/flags_coords.txt', 'r') as f:
            self.flag_coords_dict = json.load(f)

    def display_gear(self, gear_coords: list):
        
        for x, y  in gear_coords:
            self.matrix.SetPixel(x, y, 255, 0, 0)

    def display_flag(self, flag: dict):
        
        if flag == 2147745796:
            #Display green flag
            for coords in self.flag_coords_dict['green']:
                self.matrix.SetPixel(coords[0], coords[1], 0, 225, 0)
        elif flag == 268697601:
            #Display checkered flag
            for coords in self.flag_coords_dict['checkered']:
                self.matrix.SetPixel(coords[0], coords[1], 255, 255, 255)

    def select_gear(self, gear: str):
        
        try:
            gear_int = int(gear)
            self.display_gear(self.gears_coords_list[gear_int])
        except IndexError as err:
            print(f'Error 1: {err}')

    def process_data(self, data):
        try:
          
            self.matrix.Clear()
            data_str = data.decode()
            data = json.loads(data_str)
            
            self.gear = data['gear']
            self.select_gear(self.gear)
        
            self.flag = data['flags']
            self.display_flag(self.flag)
            print(f'Gear: {self.gear}Flags: {self.flag}')
        except Exception as err:
            print(f"Error 2: {err}. Data: {data}")

