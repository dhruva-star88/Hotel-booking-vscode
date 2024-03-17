import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

password = os.getenv("hotel_book_test1")
body = '''Hello,
This is the body of the email
sicerely yours
G.G.
'''
sender = 'workdhruvateja@gmail.com'
password = password
receiver = 'dhruvatej6565@gmail.com'

# Setup the MIME
message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = 'This email has an attacment, a pdf file'

message.attach(MIMEText(body, 'plain'))

pdfname = 'output.pdf'

# open the file in bynary
binary_pdf = open(pdfname, 'rb')

payload = MIMEBase('application', 'octate-stream', Name=pdfname)
payload.set_payload((binary_pdf).read())

# enconding the binary into base64
encoders.encode_base64(payload)

# add header with pdf name
payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
message.attach(payload)

# use gmail with port
session = smtplib.SMTP('smtp.gmail.com', 587)

# enable security
session.starttls()

# login with mail_id and password
session.login(sender, password)

text = message.as_string()
session.sendmail(sender, receiver, text)
session.quit()
print('Mail Sent')
