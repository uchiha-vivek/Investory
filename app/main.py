import streamlit as st
from langchain_ollama import ChatOllama
st.title("Make your financial chatbot")

with st.form("llm-form"):
    text = st.text_area("Enter your question")
    submit = st.form_submit_button("Submit")

def generate_response(input_text):
    model=ChatOllama(model='llama3.2:1b',base_url='http://localhost:11434')
    response = model.invoke(input_text)
    return response.content

if submit and text:
    response = generate_response(text)
    st.write(response)