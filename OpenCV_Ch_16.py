import cv2 as cv
cap = cv.VideoCapture(0)


# writing format, codec, video writer object and file output
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv.VideoWriter("Resources/My_Video.avi", 
                    cv.VideoWriter_fourcc("M", "J", "P", "G"), 
                    10, (frame_width, frame_height))

def fhd_resolution():
    cap.set(3, 1920)
    cap.set(4, 1080)
    cap.set(cv.CAP_PROP_FPS, 100)
fhd_resolution()

while (True):
    ret, frame = cap.read()
    if ret == True:
        cv.imshow('Camera', frame)
        out.write(frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()