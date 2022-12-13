import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open Camera")
    exit()

print([cap.get(i) for i in range(18)])
# print(cv.__dir__())

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Flip the webcam
    frame = cv.flip(frame, 1)

    # if frame is read correctly, ret is True
    if not ret:
        print("Cannot receive frame (stream end?). Exiting...")
        break

    # Operations on the frame happen here
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    # cv.imshow('frame', gray)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        print("")
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
