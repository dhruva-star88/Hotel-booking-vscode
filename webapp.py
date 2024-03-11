import streamlit as st
import requests
from streamlit_lottie import st_lottie


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