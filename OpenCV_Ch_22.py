# Chapter 22: Face Detection in Images

# step 01 - Import libraries

import cv2 as cv

face_cascade = cv.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')

# step 02 - Reading Image
img = cv.imread("Resources/Ross.jpg")

img = cv.resize(img, (250, 350))
cv.imwrite("Resized_ross.png", img)

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imwrite("gray_ross.png", gray_img)

faces = face_cascade.detectMultiScale(gray_img, 1.1, 4)

# draw rectangle
for (x, y, w, h) in faces:
    cv.rectangle(gray_img, (x,y), (x+w, y+h), (255, 0, 0), 2)

cv.imshow("Ross", gray_img)

cv.imwrite("Resources/Ross_det.png", gray_img)

cv.waitKey(0)
cv.destroyAllWindows()

