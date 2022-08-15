# Chapter 20: Splitting a Video into Frames

# step 01 - Import libraries

import cv2 as cv
import numpy as np

# step 02 - define a function
cap = cv.VideoCapture("Resources/video.mp4")

frameNr = 0

while (True):
    success, frame = cap.read()
    if success:
        cv.imwrite(f"Resources/frames/frame_{frameNr}.jpg", frame)
    else:
        break
    frameNr = frameNr+1

cap.release()



