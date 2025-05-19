from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model='gpt-4')
# model=ChatOpenAI(model='gpt-4',temperature=,max_completion_tokens=)

response=model.invoke('What is the capital of India?') #msg:str -> msg + metadata

print(response.content)

