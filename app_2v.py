## Import following libaries in venv virtual environment

from dotenv import load_dotenv
load_dotenv() ## to load all the environment variables
import streamlit as st
import os
import google.generativeai as genai 

### Pass your Google_API_KEY variable from .env 
genai.configure(api_key=os.getenv("Google_API_Key"))

### Function to load Gemini Pro model and get responses

model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text


## Initialize our streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini Application")
input=st.text_input("Input", key="input")
submit=st.button("Ask the question")

## When submit is clicked

if submit:
    response=get_gemini_response(input)
    st.subheader("The response is") 
    st.write(response)  




