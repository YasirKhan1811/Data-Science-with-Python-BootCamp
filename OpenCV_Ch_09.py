# How to connect to webcam into OpenCV in Python

# step-1 Import libraries
import cv2 as cv
import numpy as np

# step-2 Read video (frames) from webcam
cap = cv.VideoCapture(0) # webcam no. 1

# step-3 Display frame by frame
while(cap.isOpened()):
    
    # capture frame by frame
    ret, frame = cap.read()
    if ret == True:
    
        # to display frame
        cv.imshow("webcam", frame)
    
        # to quit with q key
        if cv.waitKey(25) & 0xFF == ord('q'):
            break
    
    # Break the loop
    else: 
        break

# step-4 Release or close windows
cap.release()
cv.destroyAllWindows()
