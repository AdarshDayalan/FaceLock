import cv2

def takeSnapshot(url):
    try:
        print("Getting video feed")
        cap = cv2.VideoCapture(url)
        print("Got video feed")

        while(cap.isOpened()):
            ret, frame = cap.read()
            print("Saved frame")
            imgName = "Door0" + ".png"
            cv2.imwrite(imgName, frame)
            #sendEmail.sendMail(imgName, "Face Recognition")
            print("Saved Pic")
            break

        cap.release()
        cv2.destroyAllWindows()

    except Exception as e:
        print(e)
    
