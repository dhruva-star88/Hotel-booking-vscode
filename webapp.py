import streamlit as st
import requests
from streamlit_lottie import st_lottie
import pandas as pd
from backend import Hotel, Database, PdfTicket, SendEmail, CreditCard, CardSecuirty


df = pd.read_csv("hotels.csv", dtype={"id": str})


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
    with st.form("Registration",border=False):
        # Get name
        name = st.text_input(label="Name", max_chars=30, placeholder="Please Enter Your Name")
        # Get Mobile number
        mobile_nr = st.text_input(label="Mobile Number", max_chars=10, placeholder="Please Enter your 10 digit number...")
        # Get Gmail ID
        email = st.text_input(label="Email ID", max_chars=40, placeholder="Please type your email id...")
        # Get Hotel ID
        hotel_id = st.text_input(label="Hotel ID", max_chars=3, placeholder="Please Enter The Hotel ID...")
        # Billing Details
        st.header("Please fill your billing details: ")
        # Get holder Name
        holder_name = st.text_input(label="Holder Name", max_chars=30, placeholder="Please Enter Holder Name...")
        # Get card number
        card_nr = st.text_input(label="Credit Card Number", max_chars=10, placeholder="Please Enter Card Number...")
        # Get Expiration
        expiration = st.text_input(label="Expiration Number(M/Y)", max_chars=8, placeholder="Please Enter Expiration date...") 
        # Get cvc
        cvc = st.text_input(label="CVC Number", max_chars=3, placeholder="Please Enter CVC...")
        # Card Security
        st.subheader("Enter the Card Password")
        # Get Password
        pass_wd = st.text_input(label="Password", type="password", placeholder="Please type your password...")
        # Submit Button 
        submit = st.form_submit_button("SUBMIT")
    if submit: 
        try:
            hotel = Hotel(hotel_id)
            if hotel.availability():
                credit_card = CreditCard(card_nr=card_nr,holder=holder_name, expiration=expiration, cvc=cvc)
                try:
                    if credit_card.enquire():
                        credit_details = credit_card.details()
                        card_security = CardSecuirty(card_num=credit_details[1], user_pass_wd=pass_wd)
                        if card_security.authenticate():
                            hotel.book() 
                            ticket = Database(customer_name=name, ph_number=mobile_nr, hotel_name=hotel, email_id=email)
                            details = ticket.generate()
                            ticket.store_person_details(content= details)
                            ticket.store_credit_details(details=credit_details)
                            pdf_ticket = PdfTicket(content=details)
                            pdf_ticket.pdf_generate()
                            email = SendEmail(content=details)
                            email.generate_email()
                        else:
                            st.error("Credit Card Authentication Failed..Please Try again Later..", icon="❌")
                except ValueError:
                    st.error("Enter Proper Credit Card Number", icon="☠️")
            else:
                st.warning("Hotel is Not available", icon="😔")
        except ValueError:
            st.info("Please Enter Correct ID", icon="💡")
        try:
            u_name = details[0]
            h_name = details[3]
            st.header("Your Ticket has been booked")
            st.subheader("THANK YOU FOR VISITING OUR HOTEL:")
            st.write("Here are your following Booking Deatils: ")
            st.write(f"Name: {u_name}")
            st.write(f"Hotel: {h_name}")
            st.subheader("Your Digital Ticket has been sent to your Gmail")
        except NameError:
            pass
        
        