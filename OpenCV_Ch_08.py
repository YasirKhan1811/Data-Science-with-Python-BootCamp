# Chapter 08: Converting a Video into Grayscale and Saving It to The Local Folder
# This tutorial will walk you through the step by step process, from importing/reading a 
# video to converting it to grayscale/applying some other methods and finally saving those 
# changes to the local folder. For siplicity, I am going with the same video file that I used in previous chapters.

# importing libraries
import cv2 as cv
from cv2 import VideoWriter
import numpy as np
   
# Create a VideoCapture object and read from input file
cap = cv.VideoCapture('Resources/video.mp4')

# writing format, codec, video writer object and file output
frame_width = int(cap.get(3)) # 3 is the key for width
frame_height = int(cap.get(4)) # 4 is the key for height

out = cv.VideoWriter("Resources/gray_video.avi", 
                    cv.VideoWriter_fourcc("M", "J", "P", "G"), 
                    10, (frame_width, frame_height), isColor = False) # the argument 10 is the value of fps (frames per second)

# Read the video
while (True):

    # Capture frame-by-frame
    (ret, frame) = cap.read()
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    # to show the video in player
    if ret == True:
        
        cv.imshow('Video', grayframe)
        # to quit with q key
        if cv.waitKey(25) & 0xFF == ord('q'):
            break
        # saving it
        out.write(grayframe) # this function will save our grayscale video in the local folder
   
    # Break the loop
    else: 
        break
   
# When everything done, release the video capture object
cap.release()

# out.release()
   
# Closes all the frames
cv.destroyAllWindows()