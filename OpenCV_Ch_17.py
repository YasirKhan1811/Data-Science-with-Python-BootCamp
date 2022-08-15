# 39th Day

import cv2 as cv
import numpy as np

img = cv.imread("Resources/birds.jpg")
img = cv.resize(img, (250, 200))
cv.imshow("Birds", img)
cv.imwrite("Resources/birds.jpg", img)

# stacking same image
# 1. horizontal stacking
# hor_img = np.hstack((img, img))
# cv.imshow("Birds", hor_img)
# cv.imwrite("Birs_hor.png", hor_img)

# 2. Vertical Stacking
ver_img = np.vstack((img, img))
cv.imshow("Birds", ver_img)
cv.imwrite("Birds_ver.png", ver_img)

cv.waitKey(0)
cv.destroyAllWindows()