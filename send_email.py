import smtplib, ssl
import os

def send_email(mes, email):
    host = "smtp.gmail.com"
    port = 465
    username = "tellarnav3@gmail.com"
    password = os.getenv("SMTP_PASS")
    message = f"""\
Subject: New Email from {email}

From: {email}
{mes}
"""
    receiver = "tellarnav3@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
