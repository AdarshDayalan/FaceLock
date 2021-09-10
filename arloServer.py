from arlo import Arlo
from datetime import timedelta, date
import datetime
import cv2
import sys
from imutils.video import VideoStream
from flask import Response
from flask import Flask
from flask import render_template
import threading
import argparse
import imutils
import time

USERNAME = 'adarshdayal7@gmail.com'
PASSWORD = 'Master77g!'

def getUrl():
    url = ' '
    try:
        arlo = Arlo(USERNAME, PASSWORD)
        camera = arlo.GetDevices('camera')
        basestation = arlo.GetDevices('basestation')
        url = arlo.StartStream(basestation[0], camera[0])
        
    except Exception as e:
        print(e)
    
    return str(url)
