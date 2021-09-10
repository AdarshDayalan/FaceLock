import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def sendMail(ImgFileName, sub):
    img_data = open(ImgFileName, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = sub
    msg['From'] = 'adarshdayal7@gmail.com'
    msg['To'] = 'adarshdayal7@gmail.com'
    auth = ('adarshdayal8@gmail.com', 'adarsh007')

    text = MIMEText("New Alert")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)

    s = smtplib.SMTP( "smtp.gmail.com", 587 )
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(auth[0], auth[1])
    s.sendmail('adarshdayal7@gmail.com', 'adarshdayal7@gmail.com', msg.as_string())
    s.quit()

