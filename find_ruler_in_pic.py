import numpy as np
import cv2 as cv
import cv2
import matplotlib.pyplot as plt


# https://docs.opencv.org/4.x/dc/dc3/tutorial_py_matcher.html
def do_it_with_features(img1, img2):
    # Initiate SIFT detector
    sift = cv.SIFT_create()
    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)
    # FLANN parameters
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)  # or pass empty dictionary
    flann = cv.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)
    # Need to draw only good matches, so create a mask
    matchesMask = [[0, 0] for i in range(len(matches))]
    # ratio test as per Lowe's paper
    for i, (m, n) in enumerate(matches):
        if m.distance < 0.7 * n.distance:
            matchesMask[i] = [1, 0]

    draw_params = dict(matchColor=(0, 255, 0),
                       singlePointColor=(255, 0, 0),
                       matchesMask=matchesMask,
                       flags=cv.DrawMatchesFlags_DEFAULT)

    img3 = cv.drawMatchesKnn(img1, kp1, img2, kp2, matches, None, **draw_params)

    plt.imshow(img3, ), plt.show()


# https://stackoverflow.com/questions/42162229/opencv-lines-ruler-detection
def find_edges(img):
    # Canny https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html

    edges = cv.Canny(img, 100, 200)
    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(edges, cmap='gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()


ruler = cv.imread('ruler.png', cv.IMREAD_GRAYSCALE)
image = cv.imread("photos/IMG_3179.JPG", cv.IMREAD_GRAYSCALE)

# do_it_with_features(ruler, image)
find_edges(image)
