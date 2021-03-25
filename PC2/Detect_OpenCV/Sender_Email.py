import numpy as np
import matplotlib.pyplot as plt
import cv2
import pandas as pd
import glob2
import os
from mtcnn_cv2 import MTCNN
from time import time
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.message import Message
from email.mime.text import MIMEText
import os


def send_csv(csv_pth):
    port = 465
    smtp_server = "smtp.gmail.com"
    message = MIMEMultipart("alternative")
    message['Subject'] = 'Teste Sistemas Embarcados'

    sender_email = "email.teste.soe.crowd.detect@gmail.com"
    password = 'Embarcados2021*'

    receiver_email = "gustavocre12@gmail.com"

    COMMASPACE = ', '

    message['From'] = sender_email
    message['To'] = COMMASPACE.join(receiver_email)

    with open(csv_pth) as fp:
        record = MIMEBase('application', 'octet-stream')
        record.set_payload(fp.read())
        encoders.encode_base64(record)
        record.add_header('Content-Disposition', 'attachment',
                          filename=os.path.basename(csv_pth))

    message.attach(record)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


def send_image(image_pth):
    port = 465
    smtp_server = "smtp.gmail.com"
    message = MIMEMultipart("alternative")
    message['Subject'] = 'Teste Sistemas Embarcados'

    sender_email = "email.teste.soe.crowd.detect@gmail.com"
    receiver_email = "gustavocre12@gmail.com"
    password = 'Embarcados2021*'

    img_data = open(image_pth, 'rb').read()
    message = MIMEMultipart()


    with open(image_pth, 'rb') as f:

        mime = MIMEBase('image', 'jpg', filename=image_pth.split('/')[-1])
        mime.add_header('Content-Disposition', 'attachment', filename=image_pth.split('/')[-1])
        mime.add_header('X-Attachment-Id', '0')
        mime.add_header('Content-ID', '<0>')

        mime.set_payload(f.read())
        encoders.encode_base64(mime)
        message.attach(mime)

    COMMASPACE = ', '
    message['From'] = sender_email
    message['To'] = COMMASPACE.join(receiver_email)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


def main():
    # csv = glob2.glob('../CSV_files/*.csv')[0]
    # send_csv(csv)
    img_pth = glob2.glob('../test_images/*.jpg')[0]
    send_image(img_pth)





if __name__=="__main__":
    main()