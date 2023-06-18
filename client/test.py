
from matrix_model import LEDMatrixDisplay
import json



matrix = LEDMatrixDisplay()
data = {'gear': 0, 'flags':269221888, 'abs_active': True, 'brake_bias': 55.5, 'track_temp': 23, 'pit_lim_active': 94}
data_str = json.dumps(data)
encoded_data = data_str.encode()
matrix.process_data(encoded_data)
input('enter to continue')