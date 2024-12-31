import streamlit as st


# --- PAGE SETUP ---
st.set_page_config(layout="wide")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

about_page = st.Page(
    "views/about_us.py",
    title="About Us",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    "views/questions.py",
    title="Frequently Asked Questions",
    icon=":material/question_mark:",
)
project_2_page = st.Page(
    "views/contact.py",
    title="Contact",
    icon=":material/call:",
)

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(pages=[about_page, project_1_page, project_2_page])


# --- SHARED ON ALL PAGES ---
st.logo("assets/picgentLogo.png")


# --- RUN NAVIGATION ---
pg.run()
