import numpy as np
import json

#black flag coords
pint_lim_np = np.zeros((64, 32))

pint_lim_np[0:, -3:] = 1 
rows, cols = np.where(pint_lim_np == 1)
coords_pit_lim = list(zip(rows.tolist(), cols.tolist()))



pit_lim_coords_dict  = {'pit_lim': coords_pit_lim}

with open('pit_lim_coords.txt', 'w') as f:
    json.dump(pit_lim_coords_dict, f)   