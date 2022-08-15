# Camera Setting

# Since there are different screen sizes such as Standard Definition (SD: 640 x 480), High Definition (HD: 1080 x 720), Full HD (FHD: 1920 x 1080), and Ultra High Definition (UHD) or 4K (3840 x 2160) 

# step-1 Import libraries
import cv2 as cv
import numpy as np

# step-2 Read video (frames) from webcam
cap = cv.VideoCapture(0) # webcam no. 1

cap.set(10, 100) 
# 10 is the key for brightness, and 100 is to change the brightness of screen, it can be manipulated by changing this value

cap.set(3, 1280) 
# 3 is the key for width

cap.set(4, 720) 
# 4 is the key for height

# step-3 Display frame by frame
while (True):
    (ret, frame) = cap.read()
    
    # to display frame
    if ret == True:
        cv.imshow("Video", frame)
        # to quit with q key
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    
# step-4 Release and close windows
cap.release()
cv.destroyAllWindows()
