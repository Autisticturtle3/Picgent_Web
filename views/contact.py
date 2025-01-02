import re
import streamlit as st


st.title("Contact")

def is_valid_email(email):
    # Basic regex pattern for email validation
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

with st.form("contact_form"):
    email = st.text_input("Email Address")
    message = st.text_area("Message")
    submit_button = st.form_submit_button("Submit")

if submit_button:
    if not email:
        st.error("Please provide your email address.", icon="📨")
        st.stop()

    if not is_valid_email(email):
        st.error("Please provide a valid email address.", icon="📧")
        st.stop()

    if not message:
        st.error("Please provide a message.", icon="💬")
        st.stop()
