import numpy as np
import cv2 as cv
import cv2
import matplotlib.pyplot as plt
from matplotlib import image

img = cv2.imread('IMG_3315.JPG')
image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#create the masks
mask1 = cv2.inRange(image, (0,50,20), (5,255,255))
mask2 = cv2.inRange(image, (175,50,20), (180,255,255))
mask = cv2.bitwise_or(mask1, mask2)
cropped = cv2.bitwise_and(img, img, mask=mask)

#first sliding window method
all_windows = [] 
win_size = 10
for i in range(0, cropped.shape[0]-win_size+1):
    window = cropped[i:i+win_size,:]
    all_windows.append(window)

#second sliding window method
sliding_window = []
for i in range(len(mask) - win_size + 1):
        sliding_window.append(mask[i:i+win_size])

