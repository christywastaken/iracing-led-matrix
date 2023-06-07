from rgbmatrix import RGBMatrix, RGBMatrixOptions
import time
import sys 
import numbers_for_disp
import ast

options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1 
options.parallel = 1
options.disable_hardware_pulsing = 1
options.brightness = 50

matrix = RGBMatrix(options=options)

gears_coords_list = []

with open('gears_coords.txt', 'r') as f:
      for line in f:
            line.strip()
            data_list = ast.literal_eval(line)
            gears_coords_list.append(data_list)

def display_gear(gear_coords: list):
      matrix.clear()
      for x, y  in gear_coords:
            matrix.SetPixel(x, y, 255, 0, 0)

def select_gear(gear: str):
      if gear == 'N':
            display_gear(gears_coords_list[0])
            
      
def process_data(data):
      data = data.decode()
	  print(data)