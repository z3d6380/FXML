#!/usr/bin/env python

# File: smtp.py
# Written By: Luis Moraguez
# Description: Contains all SMTP settings and methods for use with Flask App

# IMPORTS
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SMTP MAIL SETTINGS
SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = os.getenv("SMTP_PORT")
SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

def ContactMessage(firstname, email):
    message = MIMEMultipart("alternative")
    message["Subject"] = "Contact Requested"
    message["From"] = SMTP_EMAIL
    message["To"] = email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi {name},
    Thank you for reaching out!
    We will be with you shortly.
    """.format(name=firstname)
    html = """\
    <html>
    <body>
        <p>Hi <strong>{name}</strong>,<br>
        Thank you for reaching out!<br>
        We will with you shortly.
        </p>
    </body>
    </html>
    """.format(name=firstname)

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with SMTP provider and send email
    server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
    server.starttls()
    server.login(SMTP_EMAIL, SMTP_PASSWORD)
    server.sendmail(SMTP_EMAIL, email, message.as_string())