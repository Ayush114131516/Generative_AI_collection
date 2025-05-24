# Static prompt
import streamlit as st
from langchain_ollama.llms import OllamaLLM

def llm_call(text):
    llm = OllamaLLM(model="qwen2.5:7b",temperature=0.0)  
    response = llm.invoke(f"{text}")
    return response

st.header('research assistant')
user_in=st.text_input("Enter your prompt")
if st.button('Summarise'):
    st.write(llm_call(user_in))