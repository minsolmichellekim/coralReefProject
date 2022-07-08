import cv2
import numpy as np
from matplotlib import pyplot as plt


# for the below three, the image must already be in greyscale
def make_high_contrast(image):
    ret, th1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    return th1


def make_adaptive_mean(image):
    return cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)


def make_adaptive_gaussian(image):
    return cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)