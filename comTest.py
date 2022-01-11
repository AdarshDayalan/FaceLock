from socket import *
import doorPic
import garage
import button
import RPi.GPIO as GPIO
from recognize import recognize
import RPi.GPIO as GPIO
import sendEmail

servoPin = 17
buttonPin = 27
prevState = 1
currentState = 1

ctrCmd = ["L","F"]

HOST = ''
PORT = 2156
BUFSIZE = 1024
frame = 0
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(10)

num = 0

run = True

while run:

    print("Connecting...")
    tcpCliSock,addr = tcpSerSock.accept()

    while True:

        try:
            data = tcpCliSock.recv(1024)
            data = data.decode('utf-8')

            if (data is not None) & (data != ""):
                print(data)

                if data == "G":
                    tcpCliSock.send(bytes("Garage Toggling", "utf-8"))
                    tcpCliSock.close()
                    tcpCliSock,addr = tcpSerSock.accept()
                    garage.main()
                    
                elif (data == "U"):
                    tcpCliSock.send(bytes("Access granted. Unlocking", "utf-8"))
                    tcpCliSock.close()
                    tcpCliSock,addr = tcpSerSock.accept()
                    button.unlock()
                     
                elif data == ctrCmd[0]:
                    tcpCliSock.send(bytes("Locking", "utf-8"))
                    tcpCliSock.close()
                    tcpCliSock,addr = tcpSerSock.accept()
                    button.lock()
                    
                elif data == ctrCmd[1]:
                                        
                                        url = "Input camera rtsp link"
                                        
                                        tcpCliSock.send(bytes("Look at camera", "utf-8"))
                                        tcpCliSock.close()
                                        tcpCliSock,addr = tcpSerSock.accept()

                                        doorPic.takeSnapshot(url)

                                        tcpCliSock.send(bytes("Scanning facial recognition", "utf-8"))
                                        tcpCliSock.close()
                                        tcpCliSock,addr = tcpSerSock.accept()
                                        
                                        r = recognize()
                                        r.update()
                                        name, proba = r.returnFace()
                    
                                        if (name == " "):
                                                tcpCliSock.send(bytes("No face recognized", "utf-8"))
                                                tcpCliSock.close()
                                                tcpCliSock,addr = tcpSerSock.accept()
                                        else:
                                                tcpCliSock.send(bytes("Recognized " + name + " at " + "{:.2%}".format(proba), "utf-8"))
                                                tcpCliSock.close()
                                                tcpCliSock,addr = tcpSerSock.accept()

                                                if ((name == "Adarsh") or (name == "Yuvi") or (name == "Dayal") or (name == "Tommy")) & (proba >= 0.7):
                                                        tcpCliSock.send(bytes("Welcome home " + name, "utf-8"))
                                                        tcpCliSock.close()
                                                        tcpCliSock,addr = tcpSerSock.accept()
                                                        button.unlock()
                                                elif (name == "unknown"):
                                                        tcpCliSock.send(bytes("Intruder Alert", "utf-8"))
                                                        tcpCliSock.close()
                                                        tcpCliSock,addr = tcpSerSock.accept()
                                        sendEmail.sendMail("DoorF0.png", "Face Recognition")

            else:
                break

        except KeyboardInterrupt:
            tcpCliSock.close()
            button.cleanUp()
            run = False
            break


tcpCliSock.close()
