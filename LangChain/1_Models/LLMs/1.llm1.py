# this code is just for demo and can be used but NOT recommended
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv() # importing the API keys

llm=OpenAI(model='gpt-3.5-turbo-instruct')
reponse=llm.invoke('What is the capital of India?') # i/p=>msg:str

print(reponse) # o/p=>msg:str