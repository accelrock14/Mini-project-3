import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def mail(title, chapter, link, mail_id):
    sender_email = "1nh20cs096.jefersonx@gmail.com"
    receiver_email = mail_id
    password = "wsmjrjwdxzajjwfi"
    subject = title
    body = title + " " + chapter + " is out\nread now at:\n" + link

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    text = message.as_string()

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender_email, password)
        print("Logged in...")
        server.sendmail(sender_email, receiver_email, text)
        print("Email has been sent!")

    except smtplib.SMTPAuthenticationError:
        print("unable to sign in")
