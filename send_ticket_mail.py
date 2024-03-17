import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email(receiver_email):
    password = os.getenv("hotel_book_test1")
    body = '''Your Digital ticket has been generated,
    Please find it in below attched pdf.  
    '''
    sender = 'workdhruvateja@gmail.com'
    password = password
    receiver = receiver_email

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = 'Digital Reservation Ticket'

    message.attach(MIMEText(body, 'plain'))

    pdfname = 'ticket.pdf'

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

if __name__ == "__main__":
    send_email("dhruvatej6565@gmail.com")
