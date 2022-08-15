# Basic functions or Manipulation in OpenCV

# step-1 Import libraries
import cv2 as cv
from cv2 import imshow
from cv2 import imwrite
import numpy as np

# Read the image
img = cv.imread("Resources/nature.jpg")
img = cv.resize(img, (400, 250))
# cv.imshow("Nature", img)
# # cv.imwrite("Nature.png", img)


# step-3 Functions
# 1. Resize
# resized_img = cv.resize(img, (300, 200))
# cv.imshow("Resized", resized_img)
# cv.imwrite("Resized_nature.png", resized_img)

# # 2. Gray
# gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray_img)
# cv.imwrite("Gray.png", gray_img)

# 3. Blurred image
# blurr_img = cv.GaussianBlur(img, (47,47), 0)
# cv.imshow("Blurr", blurr_img)
# cv.imwrite("Blurr.png", blurr_img)

# 4. Edge detection
# edge_img = cv.Canny(img, 93,93)
# cv.imshow("Edge", edge_img)
# # imwrite("Edge.png", edge_img)

# 5. Thickness of lines
# mat_kernel = np.ones((3, 3), np.uint8)
# dilated_img = cv.dilate(edge_img, mat_kernel, iterations=1)
# cv.imshow("Dilated", dilated_img)
# # cv.imwrite("Dilated.png", dilated_img)

# # 6. Make thinner outline
# ero_img = cv.erode(dilated_img, mat_kernel, iterations=1)
# cv.imshow("Erossion", ero_img)
# cv.imwrite("Erossion.png", ero_img)



# 7. Black and White
# thresh, binary = cv.threshold(gray_img, 127, 255, cv.THRESH_BINARY)

# 8. Cropping an image
print("The shape of our image is: ", img.shape)
cropped_img = img[30:140, 110:210]

# Step-4 Release or close windows
# cv.imshow("Original", img)

# cv.imshow("Resized", resized_img)
# cv.imshow("Gray", gray_img)
# cv.imshow("Blurr", blurr_img)
# cv.imwrite("Blurr.png", blurr_img)

# cv.imshow("Edges", edge_img)
# cv.imwrite("Edge.png", edge_img)

# cv.imshow("Dilated", dilated_img)
# cv.imwrite("Dilated.png", dilated_img)

# cv.imshow("Erossion", ero_img)
# cv.imwrite("Erossion.png", ero_img)
# cv.imshow("Black and White", binary)
# cv.imwrite("Black_&_White.png", binary)
cv.imshow("Cropped", cropped_img)
cv.imwrite("Cropped.png", cropped_img)

# Step-5 Displaying Image and Closing Windows
cv.waitKey(0)
cv.destroyAllWindows()