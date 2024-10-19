import streamlit as st
import requests
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Function to fetch stock data from Yahoo Finance
def get_stock_data(symbol):
    url = f'https://yfapi.net/v6/finance/quote?symbols={symbol}'
    headers = {
        'x-api-key': 'YOUR_API_KEY'  # Replace with your Yahoo Finance API key
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data

# Set up the LLaMA model via Ollama
llm = OllamaLLM(model="llama3.2:1b")  # Specify the LLaMA model version

# Create a LangChain prompt template for stock predictions
prompt_template = PromptTemplate(
    input_variables=["stock_name", "current_price", "market_cap"],
    template="Based on the current price of {stock_name} at {current_price} with a market cap of {market_cap}, "
             "provide a brief prediction about its future performance."
)

# Create an LLM chain using the prompt and the LLM
llm_chain = LLMChain(llm=llm, prompt=prompt_template)

# Streamlit app layout
st.title("Stock Prediction App")

# User input for stock symbol
stock_name = st.text_input("Enter Stock Symbol (e.g., AAPL, GOOGL)")

if st.button("Fetch Stock Data"):
    if stock_name:
        stock_data = get_stock_data(stock_name)
        
        if 'quoteResponse' in stock_data and stock_data['quoteResponse']['result']:
            stock_info = stock_data['quoteResponse']['result'][0]
            current_price = stock_info['regularMarketPrice']
            market_cap = stock_info['marketCap']
            
            st.write(f"**Current Price:** ${current_price}")
            st.write(f"**Market Cap:** ${market_cap}")

            # Generate a prediction using the LLaMA model
            prediction = llm_chain.run({
                "stock_name": stock_name,
                "current_price": current_price,
                "market_cap": market_cap
            })
            
            st.write("### Prediction:")
            st.write(prediction)
        else:
            st.error("Stock data not found. Please check the stock symbol.")
    else:
        st.error("Please enter a stock symbol.")

