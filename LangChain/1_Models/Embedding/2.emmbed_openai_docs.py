from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(dotenv_path=Path(r'D:\LangChain\.env'))
openai_token = os.getenv("OPENAI_API_KEY")

embedding=OpenAIEmbeddings(model='text-embedding-3-small',dimensions=32,api_key=openai_token)#increase dimension value to increase context size
docs=[
    
]
result=embedding.embed_documents(docs)
print(result)
print(str(result))
