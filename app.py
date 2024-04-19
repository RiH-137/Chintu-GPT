from dotenv import load_dotenv
load_dotenv() ## ;oading all the environment variables

import streamlit as st
import os
import google.generativeai as genai
import textwrap

##configuring key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini Pro model and get repsonses
model=genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])
def get_gemini_response(question):
    
    response=chat.send_message(question,stream=True)  #stream is set to True to get the response in chunks  
    return response

## about me
def about_author():
    author_name = "Rishi Ranjan"
    author_description = textwrap.dedent(
        """
        Date-->  19/04/2024
        🌟 **About Me:**
        https://www.linkedin.com/in/rishi-rih/

🚀 Hey there! I'm Rishi, a 2nd year passionate Computer Science & Engineering Undergraduate with a keen interest in the vast world of technology. Currently specializing in AI and Machine Learning, I'm on a perpetual quest for knowledge and thrive on learning new skills.

💻 My journey in the tech realm revolves around programming, problem-solving, and staying on the cutting edge of emerging technologies. With a strong foundation in Computer Science, I'm driven by the exciting intersection of innovation and research.

🔍 Amidst the digital landscape, I find myself delving into the realms of Blockchain, crafting Android Applications, and ML projects.
 JAVA and Python . 
My GitHub profile (https://github.com/RiH-137) showcases my ongoing commitment to refining my craft and contributing to the tech community.

🏎️ Outside the digital realm, I'm a fervent Formula 1 enthusiast, experiencing the thrill of high-speed pursuits. When I'm not immersed in code or cheering for my favorite F1 team, you might find me strategizing moves on the chessboard.

📧 Feel free to reach out if you're as passionate about technology as I am. You can connect with me at 101rishidsr@gmail.com.

Let's build, innovate, and explore the limitless possibilities of technology together! 🌐✨
        """
    )

    #caling the func that display name and description
    st.write(f"**Author:** {author_name}")
    st.write(author_description)







##initialize our streamlit application

st.set_page_config(page_title="Chintu GPT",page_icon="1.png",layout="wide")
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("Select a page", ("Chintu GPT", "About the Author"))
if selected_page == "Chintu GPT":
    st.header("Chintu GPT")
    st.text("Chintu GPT can support text input.")
    st.text(" Ask any question or chat in English, Hinglish, German, Telegu-English etc. and get the answer.")
    # initialize session state for chat history if it doesn't exist
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []    #we will put all the chat history in this empty list

    input=st.text_input("Say naa...",key="input")
    submit=st.button("Chat...")

    if submit and input:
        response=get_gemini_response(input)
        # add user query and response to session state chat history
        st.session_state['chat_history'].append(("You", input))
        st.subheader("The Response is")
        for chunk in response:
            st.write(chunk.text)
            st.session_state['chat_history'].append(("Chintu", chunk.text))
    st.subheader("Coverstion...")
        
        #displying output 
    for role, text in st.session_state['chat_history']:
        st.write(f"{role}: {text}")

elif selected_page == "About the Author":

    about_author()