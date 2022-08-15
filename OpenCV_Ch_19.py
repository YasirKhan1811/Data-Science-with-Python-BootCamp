# 39th Day Part-9
# coordinates of an image or video

# step 01 - Import libraries

import cv2 as cv
import numpy as np

# step 02 - define a function
def find_coord(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        # left mouse click
        print(x, '', y)

        # how to define or print on the same image or window
        font = cv.FONT_HERSHEY_PLAIN
        cv.putText(img, str(x) + ',' + str(y), (x, y), font, 3, (255,200,0), thickness=2)

        # show the text on image and image itself
        cv.imshow("image", img)

   # for color finding
    if event == cv.EVENT_RBUTTONDOWN:
        # left mouse click
        print(x, '', y)

        font = cv.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]

        cv.putText(img, str(b) + ',' + str(g) + ',' + str(r), (x,y), font, 1, (300, 180, 50), 2)
        cv.imshow('image', img)

# final function to read the display
if __name__ == "__main__":
    # reading an image
    img = cv.imread("Resources/laptop.png", 1)

    # display the  image
    cv.imshow('image', img)

    # setting call back function
    cv.setMouseCallback("image", find_coord)
    cv.waitKey(0)
    cv.destroyAllWindows()



