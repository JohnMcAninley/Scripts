import sys
import json
from smtplib import SMTP_SSL
from email.mime.text import MIMEText


def read_cfg():
    pass


def send_text(msg_str):
    msg = MIMEText(msg_str)

    msg['Subject'] = ""
    msg['From'] = ""
    msg['To'] = ""

    server = SMTP_SSL('')
    server.ehlo()
    server.login("", "")
    text = msg.as_string()
    server.sendmail("", "", text)
    server.quit()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        send_text(str(sys.argv[1]))
    else:
        print("usage: python text.py <msg>")
