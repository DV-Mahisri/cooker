import streamlit as st
# Title of the app
st.title("Adithya's Recepie maker App")

# Text input
ingredients = st.text_input("Enter the ingredients you have with you right now : ")

import google.generativeai as genai

# Set your API key directly in the code (not recommended for production)
GOOGLE_API_KEY = "AIzaSyDOGHOBp3Aogsd2zg2ovY3gXGmzzRw5fz8"

# Configure genai with the environment variable
genai.configure(api_key=GOOGLE_API_KEY)

# Create the model
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "max_output_tokens": 1000,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    generation_config=generation_config,
)

# Start a chat session
chat_session = model.start_chat(history=[])

# Send a message and get a response
response = chat_session.send_message("Please give me exactly 3 receipies using these ingredients only "+ingredients+"just give me instructions how to cook receipie not ingredients")
receipies=response.text

# Button to submit
if st.button("Submit"):
    st.write(receipies)

