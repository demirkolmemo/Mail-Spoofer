#   CREATED BY MEXİWİST
# Librarys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import traceback
import configparser
# CFG connection
config = configparser.ConfigParser()
config.read('config.ini')
# Mail Contents
def send_mail(receiver_email, spoofed_email, spoofed_name, message, subject):
    try:
        msg = MIMEMultipart("related")
        msg['From'] = f"{spoofed_name} <{spoofed_email}>"
        msg['To'] = receiver_email
        msg['Subject'] = subject
        body = message
        msg.attach(MIMEText(body, 'plain'))
        # File Attachment
        part2 = MIMEBase('application', "oclet-stream")
        part2.set_payload(open(filepath, "rb").read())
        part2.add_header('Content-Disposition', 'attachment; filename="[File Name]"')
        encoders.encode_base64(part2)
        msg.attach(part2)
        # CFG Content
        smtp_host = config.get('SMTP', 'host')
        smtp_port = config.getint('SMTP', 'port')
        smtp_username = config.get('SMTP', 'username')
        smtp_password = config.get('SMTP', 'password')
        # Server COnnection
        server = smtplib.SMTP(smtp_host, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        text = msg.as_string()
        server.sendmail(spoofed_email, receiver_email, text)
        server.quit()
        print('Spoofed Email sent successfully to '+ str(receiver_email) + ' from ' + str(spoofed_name))
    except Exception as e:
        # Print the exception
        print(traceback.format_exc())
# Mail Content
receiver_email = '[Reciver Mail]'
spoofed_email = '[Spoofer Mail]'
spoofed_name = '[Spoofer Name]'
subject = '[Subject]'
filepath = '[attachment]'
message = """\
Text
"""

# Mail Sending
send_mail(receiver_email,spoofed_email,spoofed_name, message, subject)
#   CREATED BY MEXİWİST