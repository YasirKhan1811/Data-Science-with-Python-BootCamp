# Chapter 21: How to Detect Specfic Colors Inside Python 

# The purpose is to manage the colors of an image for selection of specific objects from that figure.


# step 01 - Import libraries

import cv2 as cv
import numpy as np

# step 02 - Reading image
img = cv.imread('Resources/room.jpg')
img = cv.resize(img, (300, 250))


# Convert into hsv (Hue, Saturation, Value)

hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)


cv.imshow("Original", img)
cv.imshow("HSV", hsv_img)

cv.imwrite("Original_img.png", img)
cv.imwrite("HSV_img.png", hsv_img)

# # sliders

# def slider():
#     pass

# path = "Resources/room.jpg"


# cv.namedWindow("Bars")
# cv.resizeWindow("Bars", 1000, 200)

# cv.createTrackbar("Hue Min", "Bars", 0,179,slider)
# cv.createTrackbar("Hue Max", "Bars", 179,179,slider)
# cv.createTrackbar("Sat Min", "Bars", 0,255,slider)
# cv.createTrackbar("Sat Max", "Bars", 255,255,slider)
# cv.createTrackbar("Val Min", "Bars", 0,255,slider)
# cv.createTrackbar("Val Max", "Bars", 255,255,slider)

# img = cv.imread(path)
# hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# # hue_min = cv.getTrackbarPos("Hue Min", "Bars")
# # print(hue_min)

# while True:
#     img = cv.imread(path)
#     hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#     hue_min = cv.getTrackbarPos("Hue Min", "Bars")
#     hue_max = cv.getTrackbarPos("Hue Max", "Bars")
#     sat_min = cv.getTrackbarPos("Sat Min", "Bars")
#     sat_max = cv.getTrackbarPos("Sat Max", "Bars")
#     val_min = cv.getTrackbarPos("Val Min", "Bars")
#     val_max = cv.getTrackbarPos("Val Max", "Bars")


#     print(hue_min, hue_max, sat_min, sat_max, val_min, val_max)

#     # to see these changes inside an image

#     lower = np.array([hue_min, sat_min, val_min])
#     upper = np.array([hue_max, sat_max, val_max])
#     mask_img = cv.inRange(hsv_img, lower, upper)
#     out_img = cv.bitwise_and(img, img, mask=mask_img)

    
#     mask_img = cv.resize(mask_img, (500, 400))
#     out_img = cv.resize(out_img, (500, 400))


#     # cv.imshow("Original", img)
#     # cv.imshow("HSV", hsv_img)

#     cv.imshow("Mask", mask_img)
    
#     cv.imshow("Final Output", out_img)

#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

cv.waitKey(0)
cv.destroyAllWindows()


