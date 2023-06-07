from rgbmatrix import RGBMatrix, RGBMatrixOptions
import time
import sys 
import os
import numbers_for_disp
from PIL import Image

# if len(sys.argv) < 2:
#     sys.exit("Require an iamge argument")
# else: 
#     image_file = sys.argv[1]

dir_path = os.path.dirname(os.path.realpath(__file__))
image_file = os.path.join(dir_path, '4.png')

image = Image.open(image_file)

options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1 
options.parallel = 1
options.disable_hardware_pulsing = 1
options.brightness = 50


matrix = RGBMatrix(options=options)
# image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
# matrix.SetImage(image.convert('RGB'))


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
