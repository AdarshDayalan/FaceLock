import os
import smtplib
import ssl
import time
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def sendMail(ImgFileName, sub):
        img_data = open(ImgFileName,'rb').read()
        msg = MIMEMultipart()
        msg['Subject'] = sub
        msg['From'] = 'adarshdayal8@gmail.com'
        msg['To'] = 'adarshdayal7@gmail.com'
        auth = ('adarshdayal8@gmail.com','adarsh007')

        text = MIMEText("New Alert")
        msg.attach(text)
        image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
        msg.attach(image)

        s = smtplib.SMTP("smtp.gmail.com", 587 )
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(auth[0], auth[1])
        s.sendmail('adarshdayal8@gmail.com', 'adarshdayal7@gmail.com', msg.as_string())
        s.quit()

def sendVideo(filename, sub):
        start = time.time()
        msg = MIMEMultipart()
        msg['To'] = 'adarshdayal7@gmail.com'
        msg['From'] = 'adarshdayal8@gmail.com'
        msg['Subject'] = sub

        msg.attach(MIMEText('video text', 'html'))

        try:
                        # Open PDF file in binary mode
                        with open(filename, "rb") as attachment:
                                                        part = MIMEBase("application", "octet-stream")
                                                        part.set_payload(attachment.read())

                        # Encode file in ASCII characters to send by email
                        encoders.encode_base64(part)

                        # Add header as key/value pair to attachment part
                        part.add_header(
                                        "Content-Disposition",
                                        "attachment; filename= {filename}",
                        )

                        msg.attach(part)
                        
        except Exception as e:
                        print("Oh no! We didn't found the attachment")

        try:
                        s = smtplib.SMTP("smtp.gmail.com", 587 )
                        context = ssl.create_default_context()
                        s.starttls(context=context)
                        s.login('adarshdayal8@gmail.com', 'adarsh007')
                        s.sendmail('adarshdayal8@gmail.com', 'adarshdayal7@gmail.com', msg.as_string())
                        print('email sent')

        except Exception as e:
                        print('stuff broke')

        finally:
                        s.quit()
                        print(time.time()-start)

#sendVideo('filename.mp4', 'bruh')
