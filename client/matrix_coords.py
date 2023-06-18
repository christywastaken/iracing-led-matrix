import json
import numpy as np 

"""
Flag coords
"""


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


"""
Gear coords
"""
#2d numpy for num '1'
image1 = np.zeros((32,32))
image1[14:17, 5:27] = 1
image1[13, 6:8] = 1
image1[12, 7] = 1

rows, cols = np.where(image1 == 1)
coords1 = list(zip(rows.tolist(), cols.tolist()))


#2d numpy for num '2'
image2 = np.zeros((32,32))

image2[8:23, 5:8] = 1
image2[20:23, 8:14] = 1
image2[8:23, 14:17] = 1 
image2[8:11, 17:23] = 1
image2[8:23, 23:26] = 1 

rows, cols = np.where(image2 == 1)
coords2 = list(zip(rows.tolist(), cols.tolist()))


#2d numpy for num '3'
image3 = np.zeros((32,32))

image3[8:23, 5:8] = 1
image3[20:23, 8:26] = 1
image3[8:23, 14:17] = 1 
image3[8:23, 23:26] = 1 

rows, cols = np.where(image3 == 1)
coords3 = list(zip(rows.tolist(), cols.tolist()))


#2d numpy for num '4'
image4 = np.zeros((32,32))

image4[16:19, 5:27] = 1
image4[8:23, 20:23] = 1
x = 15
y1 = 6
y2 = 11

for i in range(8):
	image4[x, y1:y2] = 1
	x -= 1
	y1 += 2
	y2 += 2

image4[:13,-9:] = 0

	
rows, cols = np.where(image4 == 1)
coords4 = list(zip(rows.tolist(), cols.tolist()))


#2d numpy for num '5'
image5 = np.zeros((32,32))

image5[8:23, 5:8] = 1
image5[20:23, 17:23] = 1
image5[8:23, 14:17] = 1 
image5[8:11, 8:14] = 1
image5[8:23, 23:26] = 1 

rows, cols = np.where(image5 == 1)
coords5 = list(zip(rows.tolist(), cols.tolist()))


#2d numpy for num '6'
image6 = np.zeros((32,32))

image6[8:23, 5:8] = 1
image6[20:23, 17:23] = 1
image6[8:23, 14:17] = 1 
image6[8:11, 8:23] = 1
image6[8:23, 23:26] = 1 

rows, cols = np.where(image6 == 1)
coords6 = list(zip(rows.tolist(), cols.tolist()))


#2d numpy for num 'R'
image_R = np.zeros((32,32))

image_R[8:23, 5:8] = 1
image_R[20:23, 5:17] = 1
image_R[8:23, 14:17] = 1 
image_R[8:11, 8:26] = 1

x1 = 16
x2 = 19
y1 = 15
y2 = 18

for i in range(6):
	image_R[x1:x2, y1:y2] = 1
	x1 += 1
	x2 += 1
	y1 += 2 
	y2 += 2 

image_R[:26, -6:] = 0
image_R[23:28, 5:-6] = 0

rows, cols = np.where(image_R == 1)
coords_R = list(zip(rows.tolist(), cols.tolist()))


#2d numpy for num 'N'
image_N = np.zeros((32,32))

image_N[19:22, 5:26] = 1
image_N[8:11, 5:26] = 1

x1 = 10
x2 = 12
y1 = 6 
y2 = 9
for i in range(9):
	image_N[x1:x2, y1:y2] = 1 
	x1 += 1
	x2 += 1
	y1 += 2
	y2 += 2
	

rows, cols = np.where(image_N == 1)
coords_N = list(zip(rows.tolist(), cols.tolist()))

gear_coords_list  = [coords_N, coords1, coords2, coords3, coords4, coords5, coords6, coords_R]


"""
Pit limiter coords
"""
pint_lim_np = np.zeros((64, 32))

pint_lim_np[0:, -3:] = 1
rows, cols = np.where(pint_lim_np == 1)
coords_pit_lim = list(zip(rows.tolist(), cols.tolist()))



"""
ABS coords
"""
abs_np = np.zeros((64, 32))

abs_np[:3, 4:-4] = 1
abs_np[-3:, 4:-4] = 1
   
rows, cols = np.where(abs_np == 1)
coords_abs = list(zip(rows.tolist(), cols.tolist()))



matrix_coords_dict = {'flags': flag_coords_dict, 'gears': gear_coords_list, 'pit_lim': coords_pit_lim, 'abs': coords_abs}

with open('matrix_coords.txt', 'w') as f:
    json.dump(matrix_coords_dict, f)