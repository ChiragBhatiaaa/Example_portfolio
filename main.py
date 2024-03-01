import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title ="My Webpage", page_icon=":tada:", layout ="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#Use CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}", unsafe_allow_html=True)
local_css("style.css")


#Animation
lottie_coding = load_lottieurl("https://lottie.host/281b261d-17fb-49f6-be77-1de768cbb495/XQMESfFhhe.json")

#header
with st.container():
    st.subheader("Hi, I am Chirag Bhatia :wave:")
    st.title("Software Engineer by passion")
    st.write("I am passionate about finding ways to get into DevOps and have a huge love for cloud")

# About Me
with (((st.container()))):
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write('##')
        st.write(
            """ 
            I am currently a student due to graduate in June'24 and looking forward to tech roles.
            I have been working on numerous projects which are related to the Devops and Cloud field and have an itch to excel in these domains.
            My current experience and teachings have taught me a lot about:\n
            - Programming languages and technology\n
            - Cloud Technologies, mainly Azure\n
            - Devops Tools like Docker and K8s\n
            - Databases etc.\n
            
            I am a hard working individual passionate to excel in the IT Industry and 
            if this sounds like someone who you think could benefit you than do reach out to me
            """
        )

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

#Contact Form

with st.container():
    st.write("---")
    st.header("Get In Touch")
    st.write("##")

    contact_form = """ 
    <form action="https://formsubmit.co/cbhatia206@gmail.com" method="POST">
    <input type="hidden" name = "_captcha" value ="false">
     <input type="text" name="name" placeholder = "Your name" required>
     <input type="email" name="email" placeholder = "Your email" required>
     <button type="submit">Send</button>
    </form> 
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
