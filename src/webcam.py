# Mayowa Obisesan
# Python Webcam - OpenCV
# December 13, 2022.
# OOP - Class method of Webcam script


import cv2 as cv


class WebCam:
    """ Main Webcam Class """
    WINDOW_NAME = 'Python Webcam'

    def __init__(self):
        self.webcam = cv.VideoCapture(0)
        if not self.webcam.isOpened():
            print("Cannot open Camera")
            exit()

    def run(self):
        """ Webcam method to run the webcam """
        while self.webcam:
            ret, frame = self.webcam.read()
            frame = cv.flip(frame, 1)  # 1 for x-axis, 0 for y-axis
            if not ret:
                print("Cannot receive frame. Exiting")
                break

            cv.imshow(self.WINDOW_NAME, frame)
            if cv.waitKey(1) == ord('q'):
                print("Letter q pressed. I will exit now.")
                break
        self.webcam.release()
        cv.destroyAllWindows()


if __name__ == "__main__":
    WebCam().run()
