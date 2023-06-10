import json
import numpy as np

#Green flag coords
flag_green = np.ones((64,3))

rows, cols = np.where(flag_green == 1)
coords_green = list(zip(rows.tolist(), cols.tolist()))


#Green flag coords
flag_checkered = np.ones((64,3))
x1 = 4
x2 = 9
while x2 < 64:
    flag_checkered[x1:x2:, :4] = 0 
    x1 += 4
    x2 += 4
    
rows, cols = np.where(flag_checkered == 1)
coords_checkered = list(zip(rows.tolist(), cols.tolist()))


flag_coords_dict  = {'green': coords_green, 'checkered': coords_checkered}

with open('flags_coords.txt', 'w') as f:
    json.dump(flag_coords_dict, f)