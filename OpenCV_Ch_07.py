# Chapter 07: Converting Video into Gray or Black and White

# importing libraries
import cv2 as cv
import numpy as np
   
# Create a VideoCapture object and read from input file
cap = cv.VideoCapture('Resources/video.mp4')

# Read the video
while (True):
    
    # Capture frame-by-frame
    (ret, frame) = cap.read()
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # converting
    (thresh, binary) = cv.threshold(grayframe, 127, 255, cv.THRESH_BINARY)
    if ret == True:    
        # Display the resulting frame
        cv.imshow('Video', binary)
   
        # quiting with q key
        if cv.waitKey(40) & 0xFF == ord('q'):
            break
   
    # Break the loop
    else: 
        break
   
# When everything done, release 
# the video capture object
cap.release()
   
# Closes all the frames
cv.destroyAllWindows()