from rgbmatrix import RGBMatrix, RGBMatrixOptions
import time
import sys 
import numbers_for_disp

options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1 
options.parallel = 1
options.disable_hardware_pulsing = 1
options.brightness = 50

matrix = RGBMatrix(options=options)



def display_gear(int: num):
      

for i in numbers_for_disp.number_coords_list:
	matrix.Clear()
	for x, y in i:
		matrix.SetPixel(x, y, 255, 0, 0)
	input('Press Enter to continue')
	if i == len(numbers_for_disp.number_coords_list) - 1:
		break
	
	

try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    sys.exit(0)
