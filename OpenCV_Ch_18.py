# Chapter 18: How to change the Perspective of an Image

# step 01 - Import libraries

import cv2 as cv
import numpy as np

# step 02 - define a function

img = cv.imread('Resources/laptop.png')
# print(img.shape)


width = 900
height = 600
# defining points
point1 = np.float32([[69, 143], [383, 32], [155,394], [439, 244]])

point2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv.getPerspectiveTransform(point1, point2)
out_img = cv.warpPerspective(img, matrix, (width, height))


cv.imshow('Original', img)


out_img = cv.resize(out_img, (600, 400))
cv.imshow('Transformed', out_img)
cv.imwrite('Transformed.png', out_img)


cv.waitKey(0)
cv.destroyAllWindows()



