# Chapter 01: Import an Image with OpenCV

### Importing Required Library. Here we will import only cv2. 


import cv2 as cv


### Reading an Image from Local Directory in Desktop

img = cv.imread("Resources/image.jpg")

### Showing the Image
cv.imshow("First Image", img)
cv.imwrite("First_Image.png", img)
cv.waitKey(0) # to show image for infinite time
cv.destroyAllWindows() # To turn off all opened windows