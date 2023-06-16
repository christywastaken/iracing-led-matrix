import numpy as np
import json

#black flag coords
abs_np = np.zeros((64, 32))

abs_np[:3, 4:-4] = 1
abs_np[-3:, 4:-4] = 1
    
rows, cols = np.where(abs_np == 1)
coords_abs = list(zip(rows.tolist(), cols.tolist()))



abs_coords_dict  = {'abs': coords_abs}

with open('abs_coords.txt', 'w') as f:
    json.dump(abs_coords_dict, f)