import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def mail(title, chapter, link, email_ids, src):
    sender_email = "1nh20cs096.jefersonx@gmail.com"
    password = "wsmjrjwdxzajjwfi"
    subject = title

    html = """\
            <!DOCTYPE html>
            <html>
                <body>
                    <div>
                        <h1>""" + title + """</h1>
                        <h2>""" + chapter + """</h2>
                        <p>
                            New chapter is out now on <b>MANGA Plus</b><br />
                            Click to read now.
                        </p>
                    </div>
                    <div>
                        <center>
                            <a href=""" + link + """><img src=""" + src + """/></a> <p> Read the latest chapters from our 
                            weekly magazine for free and simultaneously with Japan.<br /> Download MANGA Plus now and get 
                            started! </p> <a href="https://play.google.com/store/apps/details?id=jp.co.shueisha.mangaplus
                            "><img src="https://mangaplus.shueisha.co.jp/img/web_logo_190118_light.c773f9e9.png"/></a> 
                            <p>©︎2019 Shueisha Inc. All rights reserved. <br /></p>
                        </center>
                    </div>
                </body>
            </html> """

    for receiver_email in email_ids:
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email[0]
        message["Subject"] = subject
        message["Bcc"] = receiver_email[0]

        message.attach(MIMEText(html, "html"))
        text = message.as_string()

        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

        try:
            smtp_server.ehlo()
            smtp_server.login(sender_email, password)
            print("Logged in...")
            smtp_server.sendmail(sender_email, receiver_email[0], text)
            smtp_server.quit()
            print("Email has been sent!")
        except smtplib.SMTPAuthenticationError:
            print("unable to sign in")
