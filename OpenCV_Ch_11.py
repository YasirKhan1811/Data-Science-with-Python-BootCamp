# Reading and writing videos from Cam

# step-1 Import libraries
import cv2 as cv
import numpy as np

# step-2 Read video (frames) from webcam
cap = cv.VideoCapture(0) # webcam no. 1

# step-3 Writing format, codec, video writer object and file output
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv.VideoWriter("Resources/video.avi", cv.VideoWriter_fourcc("M", "J", "P", "G"), 20, (frame_width, frame_height))

# step-4 Display frame by frame
while (True):
    (ret, frame) = cap.read()
    
    # to display frame
    if ret == True:

        # following function will save the webcam in local folder
        out.write(frame)
        
        # displaying the frame
        cv.imshow("Video", frame)
        
        # to quit with q key
        if cv.waitKey(100) & 0xFF == ord('q'):
            break
    else:
        break
    
# step-5 Release and Close windows
cap.release()
out.release()
cv.destroyAllWindows()
