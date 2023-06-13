
from matrix_model import LEDMatrixDisplay
import json


"""
537133568 pace 
2147745796 green
268697600 racing???
269221888 black - wrong way???
268697632 blue
268697601 checkered
268697602 white 
537149440 yellow? (exxtended caution rolling start)
"""

matrix = LEDMatrixDisplay()
data = {'gear': 0, 'flags':269221888}
data_str = json.dumps(data)
encoded_data = data_str.encode()
matrix.process_data(encoded_data)
input('enter to continue')