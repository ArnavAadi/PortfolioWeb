import streamlit as st
from send_email import send_email

st.header("Contact Us")

with st.form(key="email_forms", clear_on_submit=True):
    email = st.text_input("Your Email Address")
    message = st.text_area("Your Message")
    button = st.form_submit_button()
    if button:
        send_email(message,email)
        st.info("Your email was sent successfully")