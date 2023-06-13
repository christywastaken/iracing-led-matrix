import json
import numpy as np

#plain flag coords
flag_plain = np.ones((64,3))

rows, cols = np.where(flag_plain == 1)
coords_plain = list(zip(rows.tolist(), cols.tolist()))


#checkered flag coords
flag_checkered = np.zeros((64,3))
x1 = 0
x2 = 4
while x2 < 64:
    flag_checkered[x1:x2, :4] = 1 
    x1 += 7
    x2 += 7
    
rows, cols = np.where(flag_checkered == 1)
coords_checkered = list(zip(rows.tolist(), cols.tolist()))


#black flag coords
X = np.array([[1, 0, 1],
              [0, 1, 0],
              [1, 0, 1],
              [0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]])

flag_black = np.tile(X, (16, 1))
    
rows, cols = np.where(flag_black == 1)
coords_black = list(zip(rows.tolist(), cols.tolist()))



flag_coords_dict  = {'plain': coords_plain, 'checkered': coords_checkered, 'black': coords_black}

with open('flags_coords.txt', 'w') as f:
    json.dump(flag_coords_dict, f)