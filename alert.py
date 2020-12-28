from __main__ import *
import smtplib
import ssl
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# connection port for SSL
port = 465

# account login & password (of dummy account)
login = ""
password = ""

context = ssl.create_default_context()

# Email information
sender = "AlertMonitoringSystem@gmail.com"
reciever = "pythondebugging11022@gmail.com"

# alternate version allows for html option for hyperlinks
message = MIMEMultipart("alternative")
message["Subject"] = "Best Buy Product In Stock"
text = """ Your product is in stock now!
    Time:{}""".format(datetime.now())

# Product link taken from webscraper.py
htmlMessage = """\
    <html>
        <body>
            <p>Your <a href="{}">product</a> is in stock now!
            Time:{}""".format(productLink, datetime.now())

part1 = MIMEText(text, "plain")
part2 = MIMEText(htmlMessage, "html")
message.attach(part1)
message.attach(part2)

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(login, password)
    server.sendmail(sender, reciever, message.as_string())
