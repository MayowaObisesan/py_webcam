import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open Camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # The webcam display is not mirrored, flip to simulate mirroring.
    frame = cv.flip(frame, 1)

    # if frame is read correctly, ret is True
    if not ret:
        print("Cannot receive frame (stream end?). Exiting...")
        break

    # Operations on the frame happen below

    # To show the output as grayscale
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting grayscale frame
    # cv.imshow('frame', gray)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        print("Letter Q has been pressed. I will exit now.")
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
