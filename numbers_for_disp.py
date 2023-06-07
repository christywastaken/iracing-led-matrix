import numpy as np 

#2d numpy for num '1'
image1 = np.zeros((32,32))
image1[14:17, 5:27] = 1
image1[13, 6:8] = 1
image1[12, 7] = 1

rows, cols = np.where(image1 == 1)
coords1 = list(zip(rows, cols))


#2d numpy for num '2'
image2 = np.zeros((32,32))

image2[8:23, 5:8] = 1
image2[20:23, 8:14] = 1
image2[8:23, 14:17] = 1 
image2[8:11, 17:23] = 1
image2[8:23, 23:26] = 1 

rows, cols = np.where(image2 == 1)
coords2 = list(zip(rows, cols))


#2d numpy for num '3'
image3 = np.zeros((32,32))

image3[8:23, 5:8] = 1
image3[20:23, 8:26] = 1
image3[8:23, 14:17] = 1 
image3[8:23, 23:26] = 1 

rows, cols = np.where(image3 == 1)
coords3 = list(zip(rows, cols))


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
	print(f'x={x}, y1={y1}, y2={y2}')

image4[:13,-9:] = 0

	
rows, cols = np.where(image4 == 1)
coords4 = list(zip(rows, cols))


#2d numpy for num '5'
image5 = np.zeros((32,32))

image5[8:23, 5:8] = 1
image5[20:23, 17:23] = 1
image5[8:23, 14:17] = 1 
image5[8:11, 8:14] = 1
image5[8:23, 23:26] = 1 

rows, cols = np.where(image5 == 1)
coords5 = list(zip(rows, cols))


#2d numpy for num '6'
image6 = np.zeros((32,32))

image6[8:23, 5:8] = 1
image6[20:23, 17:23] = 1
image6[8:23, 14:17] = 1 
image6[8:11, 8:23] = 1
image6[8:23, 23:26] = 1 

rows, cols = np.where(image6 == 1)
coords6 = list(zip(rows, cols))


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
coords_R = list(zip(rows, cols))


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
coords_N = list(zip(rows, cols))

number_coords_list  = [coords1, coords2, coords3, coords4, coords5, coords6, coords_R, coords_N]
