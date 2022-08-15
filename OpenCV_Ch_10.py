# Chapter 10: How to Convert Webcam into Different Shades of Gray and Black&White

### This tutorial of OpenCV will display the webcam in colored mode, grayscale, and black and white display

# step-1 Import libraries
import cv2 as cv
import numpy as np

# step-2 Read video (frames) from webcam
cap = cv.VideoCapture(0) # webcam no. 1

# step-3 Display frame by frame
while(cap.isOpened()):
    # capture frame by frame
    ret, frame = cap.read()
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    thresh, binary = cv.threshold(gray_frame, 127, 255, cv.THRESH_BINARY)
    # to display frame
    cv.imshow("OriginalCam", frame)
    cv.imshow("GrayCam", gray_frame)
    cv.imshow("Black&WhiteCam", binary)
    # to quit with q key
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
# step-4 Release or close windows
cap.release()
cv.destroyAllWindows()
