from socket import *
import doorPic
from time import ctime
import RPi.GPIO as GPIO
import os
from subprocess import call
from recognize import recognize
import cv2

ctrCmd = ["L","U"]

HOST = ''
PORT = 2156
BUFSIZE = 1024
frame = 0
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

#tspSerSock = socket(AF_INET, SOCK_STREAM)
#tspSerSock.bind((HOST,2157))
#tspSerSock.listen(5)

while True:
        print('Waiting for connection')
        tcpCliSock,addr = tcpSerSock.accept()
 #       tspCliSock,addrRecieve = tspSerSock.accept()

        try:
                while True:
                        data = tcpCliSock.recv(BUFSIZE)
                        data = data.decode("utf-8")

                        if not data:
                                break
                            
                        if str(data) == ctrCmd[0]:
                                print("Lock")
                #Lock Servo
                        elif str(data) == ctrCmd[1]:
#                                tspCliSock.send(bytes("Connecting to Arlo", "utf-8"))

                                doorPic.takeSnapshot()
                                r = recognize()
                                r.update()
                                frame = r.returnFrame()
                                cv2.imwrite('DoorF0.png', frame)
                                name, proba = r.returnFace()
                                if (name == 'Adarsh') & (proba >= 0.6):
                                    print("Unlock")
                #Unlock Servo
                        else:
                            print(data)
                                           
        except KeyboardInterrupt:
                GPIO.cleanup()
tcpSerSock.close();
