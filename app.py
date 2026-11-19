import streamlit as st
from groq import Groq
# Initialize the Groq client
GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)
MODEL="openai/gpt-oss-120b"
def get_groq_response(question):
    messages = [
        {"role": "system",
         "content": "You are an AI assistant that answers questions."
        },
        {"role": "user",
         "content": question,
        }]
    response = client.chat.completions.create( model=MODEL,messages=messages,
        max_tokens=4096)
    return response.choices[0].message.content

# Streamlit app title
st.subheader("Welcome to Akshay's Search Engine")
query = st.text_input(" ")
if st.button("Search"):
    if query:
        response = get_groq_response(query)
        st.write("Response:", response)
    else:
        st.write("Please enter a query.")
