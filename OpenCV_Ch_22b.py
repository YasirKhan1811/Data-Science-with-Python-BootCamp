# 40th Day Part-9
# Face detection in images for multiple faces

# step 01 - Import libraries

import cv2 as cv

face_cascade = cv.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')

# step 02 - Reading Image
img = cv.imread("Resources/friends.jpg")

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imwrite("gray_friends.png", gray_img)

faces = face_cascade.detectMultiScale(gray_img, 1.1, 4)

# draw rectangle
for (x, y, w, h) in faces:
    cv.rectangle(gray_img, (x,y), (x+w, y+h), (255, 0, 0), 2)

cv.imshow("friends", gray_img)

cv.imwrite("Resources/friends_faces.png", gray_img)

cv.waitKey(0)
cv.destroyAllWindows()

