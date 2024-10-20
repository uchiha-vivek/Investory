import os
import streamlit as st
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    String,
    Integer,
    select,
    insert,
)


DB_USER = "root"
DB_PASSWORD = "new_password"
DB_HOST = "localhost"
DB_PORT = 3306
DB_NAME = ""


engine = create_engine(
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
metadata_obj = MetaData()


llm = OllamaLLM(model="llama3.2")
prompt_template = PromptTemplate(
    input_variables=["stock_name", "ticker", "market_cap", "price"],
    template="Summarize the following stock information: Stock Name: {stock_name}, Ticker: {ticker}, Market Capitalization: {market_cap}, Price: {price}.",
)


llm_chain = LLMChain(llm=llm, prompt=prompt_template)


branch_stats_table = Table(
    "stocks",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("stock_name", String(50)),
    Column("ticker", String(10)),
    Column("market_cap", String(20)),
    Column("price", String(20)),
)
metadata_obj.create_all(engine)

st.title("Stock Summary App")


with engine.connect() as connection:
    result = connection.execute(select(branch_stats_table))
    if result.fetchone() is None:
        rows = [
            {
                "id": 1,
                "stock_name": "Apple Inc.",
                "ticker": "AAPL",
                "market_cap": "2.5T",
                "price": "$150",
            },
            {
                "id": 2,
                "stock_name": "Microsoft Corp.",
                "ticker": "MSFT",
                "market_cap": "2.3T",
                "price": "$280",
            },
            {
                "id": 3,
                "stock_name": "Amazon.com Inc.",
                "ticker": "AMZN",
                "market_cap": "1.8T",
                "price": "$3500",
            },
            {
                "id": 4,
                "stock_name": "Alphabet Inc.",
                "ticker": "GOOGL",
                "market_cap": "1.6T",
                "price": "$2800",
            },
        ]

        with engine.begin() as conn:
            for row in rows:
                conn.execute(insert(branch_stats_table).values(**row))


stock_name_input = st.text_input("Enter Stock Name:", "")


if stock_name_input:
    stmt = select(branch_stats_table).where(
        branch_stats_table.c.stock_name.ilike(f"%{stock_name_input}%")
    )

    with engine.connect() as connection:
        results = connection.execute(stmt).fetchall()

    if results:
        for result in results:
            stock_name, ticker, market_cap, price = (
                result[1],
                result[2],
                result[3],
                result[4],
            )
            summary = llm_chain.run(
                {
                    "stock_name": stock_name,
                    "ticker": ticker,
                    "market_cap": market_cap,
                    "price": price,
                }
            )
            st.write(f"### Summary for {stock_name} (Ticker: {ticker})")
            st.write(f"- Market Cap: {market_cap}")
            st.write(f"- Price: {price}")
            st.write(f"- Summary: {summary}")
    else:
        st.write("No stocks found with that name.")
