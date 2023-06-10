import json
import numpy as np

#Green flag coords
flag_green = np.ones((64,3))

rows, cols = np.where(flag_green == 1)
coords_green = list(zip(rows.tolist(), cols.tolist()))

flag_coords_dict  = {'green': coords_green}

with open('flags_coords.txt', 'w') as f:
    json.dump(flag_coords_dict, f)