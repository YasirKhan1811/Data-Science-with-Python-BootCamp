# Resizing the image

import numpy as np
import cv2 as cv

# How to resize an image?

# import libraries
import numpy as np
import cv2 as cv

img = cv.imread("Resources/garden.png")

# resize
resized_img = cv.resize(img, (300, 400))

# how to show an image
# cv.imshow("Original", img)
# cv.imwrite("Original.png", img)

cv.imshow("Resized", resized_img)
cv.imwrite("Resized.png", resized_img)

cv.waitKey(0) # to show image for infinite time
cv.destroyAllWindows() # To turn off all opened windows