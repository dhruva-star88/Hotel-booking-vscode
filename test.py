import sqlite3 

# Connect to the database
con = sqlite3.connect("D:\Python course\Hotel-Booking #VSCODE\data.db")
cursor = con.cursor()

# Define the data to be inserted
data = ("1", "2", "3", "5")

# Insert the data into the database
cursor.execute("INSERT INTO event1 VALUES(?, ?, ?, ?)", data)

# Commit the changes to the database
con.commit()

# Check if the data was inserted
cursor.execute("SELECT * FROM event1")
print(cursor.fetchall())

# Close the database connection
con.close()