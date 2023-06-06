from rgbmatrix import RGBMatrix, RGBMatrixOptions
import time
import sys 
import os
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


matrix = RGBMatrix(options=options)
# image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
# matrix.SetImage(image.convert('RGB'))
matrix.SetPixel(4,4, 255, 0, 0)

try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)