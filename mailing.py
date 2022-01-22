import random
import smtplib
import ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "projetssigl1@gmail.com"
password = "anas_1234"


def generate_code():
    code = random.choice(range(100000, 999999))  # generating 6-digit random code
    return code


def sendcode(receiver_email, otp):
    message = f"""\
Subject: Verification code\n
	Hello This is your verification code: {otp} """
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls()
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    return otp