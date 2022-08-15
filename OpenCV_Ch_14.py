import cv2 as cv
import numpy as np

# Draw a Canvas (0 is for black, 1 is for white canvas)
imgb = np.zeros((300, 400)) # black
# cv.imshow("Black Canvas", imgb)
# cv.imwrite("Black_Canvas.png", imgb)

# imgw = np.ones((280, 410))
# cv.imshow("White Canvas", imgw)
# cv.imwrite("White_Canvas.png", imgw)

### size of the canvas
print("The size of the black canvas is :", imgb.shape)

### Adding colors to the canvas
colored_img = np.zeros((400, 400, 3), np.uint8)
colored_img[:] = (225, 200, 55) # color complete image
colored_img[20:80, 70:340] = (255, 0, 255) # coloring part of the image

### Adding line to the canvas
cv.line(colored_img, (0,100), (400,100), (255, 0, 255), 3)
cv.line(colored_img, (0,110), (400,110), (200, 100, 60), 3) # line below the first line

### Adding Rectangle
cv.rectangle(colored_img, (100, 250), (300, 350), (100, 150, 250), 3)
cv.rectangle(colored_img, (100, 250), (300, 350), (100, 150, 250), cv.FILLED)

### Adding Circle
cv.circle(colored_img, (200, 180), 50, (50, 200, 180), 10)
cv.circle(colored_img, (200, 180), 50, (50, 200, 180), cv.FILLED)


### Adding text

cv.putText(colored_img, "Data Science with Codanics", 
            (90, 50), cv.FONT_HERSHEY_DUPLEX, 0.5, (25, 100, 60), 1)

cv.putText(colored_img, "Baba G", 
            (170, 185), cv.FONT_HERSHEY_DUPLEX, 0.5, (25, 100, 60), 1)

cv.putText(colored_img, "print(Hello World)", 
            (130, 300), cv.FONT_HERSHEY_DUPLEX, 0.5, (25, 100, 60), 1)

cv.imshow("text", colored_img)

cv.imwrite("Canvas.png", colored_img)
cv.waitKey(0)
cv.destroyAllWindows()