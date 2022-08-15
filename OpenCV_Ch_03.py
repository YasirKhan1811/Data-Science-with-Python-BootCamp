# Chapter 03: Converting an Image into Grayscale

import numpy as np
import cv2 as cv

# import an image
img = cv.imread("Resources/friends.jpg")

# Showing the original image
# cv.imshow("Original", img)

print(img.shape)

# conversion
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)



# how to show an image
cv.imshow("Gray", gray)
# cv.resize(gray, (200, 250))
cv.imwrite("gray_friends.jpg", gray)

cv.waitKey(0) # to show image for infinite time
# cv.destroyAllWindows() # To turn off all opened windows