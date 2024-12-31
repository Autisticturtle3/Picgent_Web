import streamlit as st
import pandas as pd  # pip install pandas


st.title(f"Frequently Asked Questions", anchor=False)

with st.expander("What can I do with the app?"):
    st.write(
        """
        -Explore photos about something you remember but don't know where did you save it.\n
        -Search for a photo of your ID when you need it.\n
        -Track down duplicated photos which takes space in your phone.\n
        -Find photos to make a pretty photo album.
        """
    )

with st.expander("What language does it support?"):
    st.write(
        """
        For searching functionality, we only support English. Multi-language support will be added in the future.
        """
    )

with st.expander("Will my image be saved?"):
    st.write(
        """
        Picgent never save your image, we also have option allow you to select the photo library you want to be accessed.
        """
    )
