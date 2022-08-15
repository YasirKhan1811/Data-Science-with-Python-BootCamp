# Saving an image to the local folder 

# import library
import cv2 as cv
from cv2 import resize

# import an image
img = cv.imread("Resources/birds.jpg")

# resize
img = cv.resize(img, (400, 300))

# cv.imwrite("resize_birds.jpg", img)

# conversion
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# converting a gray image to black and white
(thresh, binary) = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

# showing the image
cv.imshow("Black and White", binary)

# saving an image to the local directory
cv.imwrite("Black_and_White_birds.png", binary)

cv.waitKey(0) # to show image for infinite time
cv.destroyAllWindows() # To turn off all opened windows