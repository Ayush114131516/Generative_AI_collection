from langchain_anthropic import ChatAntropic
from dotenv import load_dotenv

load_dotenv()

model=ChatAntropic(model='claude-3.5-sonnet-20241022')
# model=ChatAntropic(model='claude-3.5-sonnet-20241022',temperature=,max_completion_tokens=)

response=model.invoke('What is the capital of India?') #msg:str -> msg + metadata

print(response.content)

