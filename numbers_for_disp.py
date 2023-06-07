import numpy as np 
image1 = np.zeros((32,32))

image1[7:25, 5:8] = 1
image1[22:25, 8:14] = 1
image1[7:25, 14:17] = 1 
image1[7:10, 17:23] = 1
image1[7:25, 23:26] = 1 


rows, cols = np.where(image1 == 1)
coords = list(zip(rows, cols))
