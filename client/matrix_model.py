from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import ast
import json
import irsdk

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
        options.brightness = 80
        options.hardware_mapping = 'adafruit-hat'
        options.show_refresh_rate = 1
        options.limit_refresh_rate_hz = 0
        
        

        self.matrix = RGBMatrix(options=options)
        self.canvas = self.matrix.CreateFrameCanvas()
        self.flags = irsdk.Flags()
        self.gears_coords_list = []
        self.flag_coords_dict = {}
        self.abs_coords_dict = {}
        

        #TODO consolidate these files into one JSON
        with open('../client/gears_coords.txt', 'r') as f:
            for line in f:
                line.strip()
                data_list = ast.literal_eval(line)
                self.gears_coords_list.append(data_list)

        with open('../client/flags_coords.txt', 'r') as f:
            self.flag_coords_dict = json.load(f)

        with open('../client/abs_coords.txt', 'r') as f:
            self.abs_coords_dict = json.load(f)


    def display_gear(self, gear_coords: list):
        for x, y  in gear_coords:
            self.canvas.SetPixel(x, y, 255, 0, 0)


    def display_flag(self, flag):
        try:
            #TODO: change to allow for multiple flags displayed.
             #if checkered flag bit is set
            if (flag & self.flags.yellow) or (flag & self.flags.yellow_waving) or (flag & self.flags.caution) or (flag & self.flags.caution_waving) != 0:
                #display yellow flag
                for coords in self.flag_coords_dict['plain']:
                    self.canvas.SetPixel(coords[0], coords[1], 255, 200, 0) 
            elif (flag & self.flags.black) or (flag & self.flags.disqualify) or (flag & self.flags.furled) != 0:
                #display black flag
                for coords in self.flag_coords_dict['black']:
                    self.canvas.SetPixel(coords[0], coords[1], 255, 255, 255)
            elif flag & self.flags.blue != 0:
                #display blue flag
                for coords in self.flag_coords_dict['plain']:
                    self.canvas.SetPixel(coords[0], coords[1], 0, 200, 255)
            elif flag & self.flags.green != 0: #if green flag bit is set
                #Display green flag
                for coords in self.flag_coords_dict['plain']:
                    self.canvas.SetPixel(coords[0], coords[1], 0, 225, 0)
            elif flag & self.flags.checkered != 0:
                #Display checkered flag
                for coords in self.flag_coords_dict['checkered']:
                    self.canvas.SetPixel(coords[0], coords[1], 255, 255, 255)
            elif flag & self.flags.white != 0:
                #Display white flag
                for coords in self.flag_coords_dict['plain']:
                    self.canvas.SetPixel(coords[0], coords[1], 255, 255, 255)
            
        except Exception as err:
            print(f'Error 4: {err}')


    def select_gear(self, gear: str):
        try:
            gear_int = int(gear)
            self.display_gear(self.gears_coords_list[gear_int])
        except IndexError as err:
            print(f'Error 1: {err}')


    def display_abs(self, abs_active: bool):
        try:
            if abs_active:
                for coords in self.abs_coords_dict['abs']:
                    self.canvas.SetPixel(coords[0], coords[1], 255, 0, 255)
        except Exception as err:
            print(f"Error 5: {err}")


    def display_bb(self, brake_bias: float):
        try:
            font = graphics.Font()
            font.LoadFont('../rpi-rgb-led-matrix/fonts/5x8.bdf')
            text_colour = graphics.Color(255,255,255)
            x = 30
            y = 20
            text = str(brake_bias)
            graphics.DrawText(self.canvas, font, x, y, text_colour, text)
            
        except Exception as err:
            print(f"Error 6: {err}")


    def process_data(self, data):
        try:
            #TODO worth implementing only clearing the pixels that are being replaced?
        
            self.matrix.Clear()
            data_str = data.decode()
            data = json.loads(data_str)
            
            gear = data['gear']
            flag = data['flags']
            abs_active = data['abs_active']
            brake_bias = data['brake_bias']
            print(f'Gear: {gear} | Flags: {flag}')

            self.select_gear(gear)
            self.display_flag(flag)
            self.display_abs(abs_active)
            self.display_bb(brake_bias)
            self.matrix.SwapOnVSync(self.canvas)
        except Exception as err:
            print(f"Error 2: {err}. Data: {data}")

