from smtplib import SMTP_SSL

from email.mime.text import MIMEText

def send_text(msg_str):
    msg = MIMEText(msg_str)

    msg['Subject'] = ""
    msg['From'] = "johnbert314@yahoo.com"
    msg['To'] = "3014529198@vext.com"

    server = SMTP_SSL('smtp.mail.yahoo.com')
    server.ehlo()
    server.login("johnbert314", "Buster314")
    text = msg.as_string()
    server.sendmail("johnbert314@yahoo.com", "3014529198@vtext.com", text)
    server.quit()

if __name__ == "__main__":
    send_text(str(sys.argv))
