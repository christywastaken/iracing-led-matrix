from rgbmatrix import RGBMatrix, RGBMatrixOptions 
import ast

options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1 
options.parallel = 1
options.disable_hardware_pulsing = 1
options.brightness = 50
options.hardware_mapping = 'adafruit-hat'

matrix = RGBMatrix(options=options)

gears_coords_list = []

with open('../client/gears_coords.txt', 'r') as f:
    for line in f:
        line.strip()
        data_list = ast.literal_eval(line)
        gears_coords_list.append(data_list)

def display_gear(gear_coords: list):
    matrix.Clear()
    for x, y  in gear_coords:
        matrix.SetPixel(x, y, 255, 0, 0)

def select_gear(gear: str):
    try:
        if gear == 'N':
            display_gear(gears_coords_list[0])
        elif gear == 'R':
            display_gear(gears_coords_list[-1])
        else:
            gear_int = int(gear)
            display_gear(gears_coords_list[gear_int])
    except IndexError as err:
        print(f'Error: {err}')
      
def process_data(data):
     data = data.decode()
     select_gear(data)
