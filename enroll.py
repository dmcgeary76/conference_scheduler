from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from time import sleep
import csv


def send_it(recipient):
    sender_email = "dmcgeary@hcde-texas.org"
    receiver_email = recipient
    password = "Phraenquelynne11!"

    message = MIMEMultipart("alternative")
    message["Subject"] = "ECWC Session Scheduler"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Greetings!

    We are so excited to see you this Saturday at the 33rd Annual Early Childhood Winter Conference!

    To help you prepare for all of the great sessions offered at this year's conference, we have opened up access to a Conference Session registration tool. This tool provides in-depth information about all of the day's sessions including the option to grab a seat before the day's events. You don't need to use this tool to attend sessions, but individuals who are registered through this tool will be guaranteed a seat in their chosen sessions.

    To login to this app, just follow the link below (input your email address using only lowercase letters):
    ECWC Scheduler (https://ecwc-2019-scheduler.herokuapp.com/)

    If you have any issues using this app, please contact the administrator at dmcgeary@hcde-texas.org.

    Have a great week and we'll see you on Saturday!

    Sincerely,
    The ECWC Team"""
    html = """\
    <html>
      <body>
        <p>
    Greetings!<br /><br />
    We are so excited to see you this Saturday at the 33rd Annual Early Childhood Winter Conference!<br /><br />
    To help you prepare for all of the great sessions offered at this year's conference, we have opened up access to a Conference Session registration tool.  This tool provides in-depth information about all of the day's sessions including the option to grab a seat before the day's events.  You don't need to use this tool to attend sessions, but individuals who are registered through this tool will be guaranteed a seat in their chosen sessions.<br /><br />
    To login to this app, just follow the link below (input your email address using only lowercase letters):<br />
    <a href="https://ecwc-2019-scheduler.herokuapp.com/">ECWC Scheduler</a><br /><br />
    If you have any issues using this app, please contact the administrator at dmcgeary@hcde-texas.org.<br /><br />
    Have a great week and we'll see you on Saturday!<br /><br />

    Sincerely,<br />
    The ECWC Team
        </p>
      </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )


def enroll_them():
    dataReader = csv.reader(open('roll_call.csv'), delimiter=',', quotechar='"')
    for item in dataReader:
        try:
            user = get_object_or_404(User, username=item[2].lower())
            print(item[2] + ' already exists.') 
            pass
        except
            user = User(
                last_name   = item[0],
                first_name  = item[1],
                username    = item[2].lower(),
                email       = item[2].lower(),
            )
            user.set_password('ecwc2019!')
            user.save()
            send_it(item[2])
            print('Email sent to ' + item[2])
            sleep(5)
            
