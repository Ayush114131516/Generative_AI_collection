from langchain_huggingface import HuggingFaceEmbeddings
import os

os.environ['HF_HOME'] = 'D:/huggingface_cache'

embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
text='India is my country'
vector=embedding.embed_query(text)
print(len(vector))

docs=[
    'Grape jelly was leaking out the hole in the roof.',
    'He decided to live his life by the big beats manifesto.',
    'Do not piss in my garden and tell me you are trying to help my plants grow.'
]
vector2=embedding.embed_documents(docs)
print(len(vector2))