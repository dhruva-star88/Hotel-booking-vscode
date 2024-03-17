import pandas as pd
import sqlite3 as sq
from ticket_pdf import pdf_gen
from send_ticket_mail import send_email

df = pd.read_csv("Hotels.csv", dtype={"id": str})

class Hotel:
    def __init__(self, id):
        self.hotel_id = id
        self.hotel_name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def availability(self):
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

class ReservationTicket:
    def __init__(self, customer_name, hotel_name, ph_number, email_id):
        self.customer_name = customer_name
        self.hotel_name = hotel_name
        self.ph_number = ph_number
        self.email_id = email_id
        
    def generate(self):
        content = self.customer_name, self.ph_number,self.email_id, self.hotel_name.hotel_name
        return content

class Database(ReservationTicket):
    def store(self, content):
        connection = sq.connect("D:\Python course\hotel-booking in vscode\data.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO event1 VALUEs(?,?,?,?)", content)
        connection.commit()
        connection.close

class PdfTicket:
    def __init__(self, content):
        self.content = content
    
    def pdf_generate(self):
        return pdf_gen(self.content)

class SendEmail:
    def __init__(self, content):
        self.content = content

    def generate_email(self):
        send_email(receiver_email=self.content[2])

if __name__ == "__main__":
    print(df)
    hotel = Hotel("134")
    if hotel.availability():
        print(hotel.availability())
        hotel.book()
        ticket = Database( customer_name="Dhruva",hotel_name=hotel,ph_number="8867291499", email_id="dhruvatej6565@gmail.com")
        content = ticket.generate()
        print(content)
        ticket.store(content=content)
        pdf_ticket = PdfTicket(content=content)
        pdf_ticket.pdf_generate()
        email = SendEmail(content=content)
        email.generate_email()
         