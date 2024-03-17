import streamlit as st
import requests
from streamlit_lottie import st_lottie
import pandas as pd
from backend import Hotel, Database, PdfTicket, SendEmail

#from streamlit.connections import SQLConnection

df = pd.read_csv("hotels.csv", dtype={"id": str})
#st.connection(name="sql", type=SQLConnection)

def load_lottie_url(url):
    r = requests.get(url)
    return r.json()

animation = load_lottie_url(url="https://lottie.host/6ecdfe85-0399-4399-ab4a-d48a5ff56673/ITC1k9vVUX.json")

st.set_page_config(page_title="Hotel Booking",initial_sidebar_state="auto", layout="wide",page_icon=":hotel:")
st.title("Welcome to hotel Booking Management")
st.header("")

right_col, left_col = st.columns(2)
with right_col:
    st.image("2.jpg", width=690)

with left_col:
    st_lottie(animation, height=250, width=700, key="coding",speed=1)

st.header("Hotels Available For Booking: ")
# Load Dataframe in webpage
st.dataframe(df, hide_index=True, width=1500)
# Regestration
st.header("Please do your Registration: ")
col1, col2 = st.columns(2)
with col1:
    with st.form("Registration"):
        # Get name
        name = st.text_input(label="Name", max_chars=30, placeholder="Please Enter Your Name")
        # Get Mobile number
        mobile_nr = st.text_input(label="Mobile Number", max_chars=10, placeholder="Please Enter your 10 digit number...")
        # Get Gmail ID
        email = st.text_input(label="Email ID", max_chars=40, placeholder="Please type your email id...")
        # Get Hotel ID
        hotel_id = st.text_input(label="Hotel ID", max_chars=3, placeholder="Please Enter The Hotel ID...")
        submit = st.form_submit_button("SUBMIT")
    if submit: 
        try:
            hotel = Hotel(hotel_id)
            if hotel.availability():
                hotel.book() 
                ticket = Database(customer_name=name, ph_number=mobile_nr, hotel_name=hotel, email_id=email)
                details = ticket.generate()
                ticket.store(content= details)
                pdf_ticket = PdfTicket(content=details)
                pdf_ticket.pdf_generate()
                email = SendEmail(content=details)
                email.generate_email()
            else:
                st.warning("Hotel is Not available", icon="😔")
        except ValueError:
            st.info("Please Enter Correct ID", icon="💡")

        st.header("Your Ticket has been booked")
        st.subheader("THANK YOU FOR VISITING OUR HOTEL:")
        st.write("Here are your following Booking Deatils: ")
        st.write(f"Name: {details[0]}")
        st.write(f"Hotel: {details[3]}")
        st.subheader("Your Digital Ticket has been sent to your Gmail")
     