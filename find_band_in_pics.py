import numpy as np
import cv2 as cv
import cv2
import matplotlib.pyplot as plt

# Red mask!
# https://docs.opencv.org/4.x/dc/dc3/tutorial_py_matcher.html

img1 = cv.imread("photos/IMG_3158.JPG", cv.IMREAD_GRAYSCALE)  # queryImage
img2 = cv.imread('band.jpg', cv.IMREAD_GRAYSCALE)  # trainImage

image = cv2.imread("photos/IMG_3158.JPG")
result = image.copy()
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

red_lower = np.array([155, 25, 0])
red_upper = np.array([179, 255, 255])
red_mask = cv2.inRange(image, red_lower, red_upper)
result = cv2.bitwise_and(result, result, mask=red_mask)

# cv2.imshow('original', image)
cv2.imshow('red_mask', red_mask)
cv2.imshow('result', result)
cv2.waitKey()
