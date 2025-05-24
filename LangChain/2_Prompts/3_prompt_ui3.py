import streamlit as st
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import load_prompt

def llm_call(prompt):
    llm = OllamaLLM(model="qwen2.5:7b",temperature=0.0)  
    response = llm.invoke(prompt)
    return response

st.header('🤖Research assistant')

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )
style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 
length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

#template
template=load_prompt(r'D:\LangChain\Prompts\template.json')

prompt=template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
})

if st.button('Summarise'):
    st.write(llm_call(prompt=prompt))