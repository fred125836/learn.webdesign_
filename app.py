from PIL import Image
import requests
import streamlit as st
from strealmit_lottie import st_lottie

# find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Hello World", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/fc0153da-fac2-4fdb-bebb-7baf6d15a175/91AkjmPx5Y.json")
img_contact_form = Image.open("images/microsoft_office.jpeg")
img_lottie_animation = Image.open("images/web_dev.png")
# ---- HEADER SECTION ----
with st.container():
    st.subheader("My name is Hoodricch :wave:")
    st.title("I am a Typist, Graphic Designer, and Forex Enthusiast from Nigeria")
    st.write("I am passionate about Web Development")
    st.write("you are welcome to my page")
    st.write("[contact me on whatsapp >](https://wa.me/message/CL576QP54YBPP1)")
# ---- RANDOM ----
with st.container():
    st.write("---")
    left_column, right_column = st.column(2)
    with left_column:
        st.header("RANDOM")
        st.write("##")
        st.write(
            """
            ON MY WHATSAPP CHANNEL
            - WANT TO LEARN DATA ANALYSIS & DATA SCIENCE TO PERFORM MEANINGFUL AND IMPACTFUL ANALYSIS
            - ARE YOU STRUGGLING WITH REPETITIVE TASK IN EXCEL
            - ARE YOU WORKING WITH EXCEL AND FOUND YOURSELF THINKING  - "THESE HAS TO BE A BETTER WAY
            IF THIS SOUND INTEREESTING TO YOU, KINDLY CONTACT ME ABOVE
            """
        )
        with right_column:
            st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("MY PROJECT")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("CONTACT ME IF YOU ARE INTERESTED IN ANY OF MY SERVICES BELOW")
        st.write(
            """
            WHAT YOU WILL BE LEARNING FROM ME
            - I WILL TEACH YOU HOW TO DEVELOP WEBSITE WITH PYTHON USING PYCHARM
            - I WILL TEACH YOU GRAPHIC DESIGN WITH CORELDRAW AND CANVA
            - I WILL TEACH YOU HOW TO USE MICROSOFT OFFICES (WORD, EXCEL AND POWERPOINT)
            """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("WHAT YOU WILL BE LEARNING IN THE MICROSOFT OFFICE PACKAGE")
        st.write(
            """
            - LEARN HOW TO TYPE AND EDIT DOCUMENT IN MICROSOFT WORD
            - LEARN HOW TO MAKE ANIMATION WITH POWERPOINT
            - LEARN HOW TO USE SPREADSHEET WITH EXCEL
            """
        )
# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get in touch with me")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/jessicasmith22025@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your message here" required></textarea>
         <textarea name="schoolname" placeholder="your school name here" required></textarea>
         <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
