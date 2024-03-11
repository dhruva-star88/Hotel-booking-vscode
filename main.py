import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})

class Hotel:

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id]["name"].squeeze()

    def available(self):
        availability = df.loc[df["id"] == self.hotel_id]["available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)


class ReservationTicket:

    def __init__(self, customer_name, hotel_name):
        self.name = customer_name
        self.hotel_name = hotel_name

    def generate(self):
        content = f"""
        Thank you for visiting our Hotel
        Here Your Booking info:
        Name: {self.name}
        Hotel: {self.hotel_name.name}
        """
        return content


print(df)
hotel_ID = input("Enter the Hotel id: ")
hotel = Hotel(hotel_ID)
if hotel.available():
    hotel.book()
    name = input("Enter your Name: ")
    ticket = ReservationTicket(name, hotel)
    print(ticket.generate())
else:
    print("Hotel is not avialable")
