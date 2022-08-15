# Converting an image into black and white image

# import library
import cv2 as cv

# import an image
img = cv.imread("Resources/friends.jpg")


# conversion
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

(thresh, binary) = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
# how to show an image
cv.imshow("Black and White", binary)
# cv.imwrite("Friends26.jpg", binary)

cv.waitKey(0) # to show image for infinite time
cv.destroyAllWindows() # To turn off all opened windows