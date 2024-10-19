import os
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, select, insert


DB_USER = "root"
DB_PASSWORD = ""
DB_HOST = "localhost"   
DB_PORT = 3306         
DB_NAME = ""


engine = create_engine(f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
metadata_obj = MetaData()


llm = OllamaLLM(model="llama3.2:1b")  


prompt_template = PromptTemplate(
    input_variables=["major", "minor", "branch_name"],
    template="Summarize the following academic details: Major: {major}, Minor: {minor}, Branch: {branch_name}."
)


llm_chain = LLMChain(llm=llm, prompt=prompt_template)


branch_stats_table = Table(
    "branch_stats",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("major", String(50)),
    Column("minor", String(50)),
    Column("branch_name", String(50)),
)
metadata_obj.create_all(engine)


rows = [
    {"id": 1, "major": "Computer Science", "minor": "Mathematics", "branch_name": "Engineering"},
    {"id": 2, "major": "Electrical Engineering", "minor": "Physics", "branch_name": "Engineering"},
    {"id": 3, "major": "Business Administration", "minor": "Marketing", "branch_name": "Business"},
    {"id": 4, "major": "Psychology", "minor": "Sociology", "branch_name": "Arts"},
]

with engine.begin() as connection:
    for row in rows:
        connection.execute(insert(branch_stats_table).values(**row))

stmt = select(branch_stats_table.c.major, branch_stats_table.c.minor, branch_stats_table.c.branch_name)
with engine.connect() as connection:
    results = connection.execute(stmt).fetchall()


for result in results:
    major, minor, branch_name = result
    summary = llm_chain.run({
        "major": major,
        "minor": minor,
        "branch_name": branch_name
    })
    print(f"Summary for {major} (Minor: {minor}, Branch: {branch_name}): {summary}")
