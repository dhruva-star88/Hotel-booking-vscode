import pandas as pd

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

if __name__ == "__main__":
    print(df)
    hotel = Hotel("134")
    if hotel.availability():
        print(hotel.availability())
        hotel.book()