import streamlit as st
from streamlit_carousel import carousel

st.markdown(
    """
    <style>
    .centered {
        text-align: center;
    }
    h1 {
        font-size: 60px;
    }
    h2 {
        font-size: 50px;
    }
    p {
        font-size: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<h1 class="centered">Picgent</h1>', unsafe_allow_html=True)
st.markdown('<p class="centered">Effortlessly search your photo library like never before</p>', unsafe_allow_html=True)

picegent_examples = [
    dict(
        title="",
        text="",
        img="assets/example1.png",
    ),
    dict(
        title="",
        text="",
        img="assets/example2.png",
    ),
    dict(
        title="",
        text="",
        img="assets/example3.png",
    ),
    dict(
        title="",
        text="",
        img="assets/example4.png",
    ),
]

carousel(items=picegent_examples, interval=3000, container_height=1000, width=0.3, controls=False)

col1, col2 = st.columns(2, gap="small", vertical_alignment="top")

with col1:
    st.write("\n")
    st.subheader("AI-Powered Search", anchor=False)
    st.write(
        """
        Let PicGent find exactly what you're looking for in seconds. Search by keyword, date, location, or even objects in the image.
        """
    )

with col2:
    st.write("\n")
    st.subheader("Your Photos, Simplified", anchor=False)
    st.write(
        """
        No more scrolling endlessly! Whether it’s that beach vacation or a special moment with friends, PicGent brings your memories to you instantly.
        """
    )

with col1:
    st.write("\n")
    st.subheader("Smart & Intuitived", anchor=False)
    st.write(
        """
        Powered by advanced AI, PicGent understands your photos like you do—making organization a breeze.
        """
    )

with col2:
    st.write("\n")
    st.subheader("Start Searching Smarter Today", anchor=False)
    st.write(
        """
    Download PicGent and experience a new way to rediscover your photo library.
    Because every picture tells a story—find yours with PicGent.
        """
    )
