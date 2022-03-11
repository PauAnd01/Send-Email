#import libraries

import smtplib
import argparse

from datetime import datetime, timedelta
from email.message import EmailMessage

#Argparse to send the e-mail
parser = argparse.ArgumentParser(description='Send email')
parser.add_argument(
  '--to', dest='to_address',
  type=str, help="TO address", required=True)
parser.add_argument(
  '--title', dest='title',
  type=str, help="EMail title", required=True)
parser.add_argument(
  '--body', dest='body',
  type=str, help="Message body", required=True)

args = parser.parse_args()

msg = EmailMessage()
msg.set_content(args.body)

msg['Subject'] = args.title
msg['To'] = args.to_address

#My email acount 
sender_email_address = "paula.developing@gmail.com" 
email_password = "Emanuel_01_04"

# Set smtp server and port
email_smtp = "smtp.gmail.com"  
server = smtplib.SMTP(email_smtp, '587')

# Identify this client to the SMTP server 
server.ehlo() 

# Secure the SMTP connection 
server.starttls()

#Login to Email acount 
server.login(sender_email_address, email_password)

#Send Email
server.send_message(msg)

#Close conection to server
server.close()