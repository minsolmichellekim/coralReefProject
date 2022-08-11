import numpy as np
import cv2 as cv
import cv2
import matplotlib.pyplot as plt
from matplotlib import image

#read in image
img = cv2.imread('IMG_3315.JPG')
image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#create the masks
mask1 = cv2.inRange(image, (0,50,20), (5,255,255))
mask2 = cv2.inRange(image, (175,50,20), (180,255,255))
mask = cv2.bitwise_or(mask1, mask2)
cropped = cv2.bitwise_and(img, img, mask=mask)

#create the dense mask
dense_mask = np.zeros(mask.shape, dtype = int)

for y in range(mask.shape[0]): 
    y_min = max(0, y - 5)
    y_max = min(y + 5, mask.shape[0] - 1)
    for x in range(mask.shape[1]):
        x_min = max(0, x - 5)
        x_max = min(x + 5, mask.shape[1] - 1)
        count = 0
        for y2 in range(y_min, y_max):
            for x2 in range(x_min, x_max):
                # print(x_min, x_max)
                if mask[y2][x2] > 0:
                    count += 1
        if count > 10:
            dense_mask[y][x] = 1

cv2.imwrite("dense_mask.png", dense_mask)






