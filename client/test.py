
from matrix_model import process_data
import json

data = {'gear': 0, 'flag':'green'}
data_str = json.dumps(data)
encoded_data = data_str.encode()
process_data(encoded_data)
input('enter to continue')