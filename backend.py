import pandas as pd
import sqlite3 as sq
from ticket_pdf import pdf_gen
from send_ticket_mail import send_email

df = pd.read_csv("Hotels.csv", dtype={"id": str})
df_cards = pd.read_csv("cards.csv", dtype=str)
df_sec_card = pd.read_csv("card_security.csv", dtype=str)

connection = sq.connect("D:\Python course\hotel-booking in vscode\data.db", check_same_thread=False)

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

class CreditCard:
    def __init__(self, card_nr, holder, expiration, cvc):
        self.card_nr = card_nr
        self.holder = holder
        self.expiration = expiration
        self.cvc = cvc
    def enquire(self):
        enquire = df_cards.loc[df_cards["number"] == self.card_nr, "number"].squeeze()
        if enquire == self.card_nr:
            return True
        else:
            return False
    def details(self):
        return self.holder, self.card_nr, self.expiration, self.cvc
    
class CardSecuirty:
    def __init__(self, card_num, user_pass_wd):
        self.card_nr = card_num
        self.user_pass_wd= user_pass_wd
    
    def authenticate(self):
        pass_wd = df_sec_card.loc[df_sec_card["number"] == self.card_nr, "password"].squeeze()
        if pass_wd == self.user_pass_wd:
            return True 
        else:
            return False

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
    def store_person_details(self, content):
        cursor = connection.cursor()
        cursor.execute("INSERT INTO event1 VALUEs(?,?,?,?)", content)
        connection.commit()
        connection.close
    def store_credit_details(self, details):
        cursor = connection.cursor()
        cursor.execute("INSERT INTO event2 VALUEs(?,?,?,?)", details)
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
    print(hotel.availability())
    if hotel.availability():
        credit_card = CreditCard(card_nr="1234", holder="JOHN SMIT", expiration="12/26", cvc="123")
        print(credit_card.enquire())
        if credit_card.enquire():
            credit_details = credit_card.details()
            print(credit_details[1])
            card_security = CardSecuirty(card_num=credit_details[1], user_pass_wd="mypass")
            print(card_security.authenticate())
            if card_security.authenticate():
                hotel.book()
                ticket = Database( customer_name="Dhruva",hotel_name=hotel,ph_number="8867291499", email_id="dhruva@gmail.com")
                content = ticket.generate()
                print(content)
                ticket.store_person_details(content=content)
                print(credit_details)
                ticket.store_credit_details(details=credit_details)
                pdf_ticket = PdfTicket(content=content)
                pdf_ticket.pdf_generate()
                email = SendEmail(content=content)
                email.generate_email()
         