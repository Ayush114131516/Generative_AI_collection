from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

from pathlib import Path
import os
load_dotenv(dotenv_path=Path(r'D:\LangChain\.env'))
hf_token = os.getenv("HF_TOKEN")


from langchain_huggingface import HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    huggingfacehub_api_token=hf_token 
)

model=ChatHuggingFace(llm=llm)
response=model.invoke('What is the capital of India?')
print(response.content)