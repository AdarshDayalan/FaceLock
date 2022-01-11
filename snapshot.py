import cv2
import os

class snap:
    def __init__(self):
        self.imgName = ' '
        self.path = '/home/pi/Downloads/opencv-face-recognition/door_images'

    def takeSnap(self, url, i):
        try:
            cap = cv2.VideoCapture(url)

            while(cap.isOpened()):
                ret, frame = cap.read()
                print("i: " + str(i))
                self.imgName = "Snap" + str(i) + ".png"
                cv2.imwrite(os.path.join(self.path, self.imgName), frame)
                break
            
            cap.release()
            cv2.destroyAllWindows()

        except Exception as e:
            print(e)
            
        return self.imgName

