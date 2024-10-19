from groq import Groq
import base64
import os
from dotenv import load_dotenv
import streamlit as st

# Load environment variables from .env file
load_dotenv()

# Initialize Groq client with API key
client = Groq(api_key='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')

def analyze_financial_image(image_bytes):
    # Convert the image to base64
    base64_image = base64.b64encode(image_bytes).decode('utf-8')

    # Send request to Groq API to identify financial insights
    response = client.chat.completions.create(
        model="llama-3.2-11b-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Identify the financial insights from this image. 'Only the financial insights' comma separated and nothing else."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        stream=False,
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stop=None,
    )

    return response.choices[0].message.content

def suggest_financial_insights(financial_data):
    # Send the financial data to Llama3.2 to get further financial insights
    response = client.chat.completions.create(
        model="llama-3.2-11b-text-preview",
        messages=[
            {"role": "user", "content": f"Suggest financial insights based on the following data: {financial_data}"}
        ]
    )
    return response.choices[0].message.content


# Streamlit UI
st.title("AI-Powered Financial Insights")

uploaded_files = st.file_uploader("Upload financial document images", accept_multiple_files=True, type=["png", "jpg", "jpeg"])

if uploaded_files:
    financial_insights_list = []

    for uploaded_file in uploaded_files:
        # Analyze each uploaded image
        image_bytes = uploaded_file.read()
        financial_insights = analyze_financial_image(image_bytes)
        financial_insights_list.append(financial_insights)
        st.write(f"Identified Financial Insights in {uploaded_file.name}: {financial_insights}")

    # Suggest further insights based on the financial analysis
    if financial_insights_list:
        all_financial_data = ", ".join(financial_insights_list)
        st.write(f"All identified financial data: {all_financial_data}")
        further_insights = suggest_financial_insights(all_financial_data)
        st.write("Suggested Financial Insights:")
        st.write(further_insights)
