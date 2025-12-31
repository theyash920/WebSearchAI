import os
import streamlit as st
from langchain_groq import chat_groq 

class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input
        self.model = None

    def get_llm_model(self):
        try:
            groq_api_key = self.user_controls_input["GROQ_API_KEY"]
            selected_groq_model = self.user_controls_input["selected_groq_model"]
            if groq_api_key =='' and os.environ['GROQ_API_KEY'] =='':
                st.error("please enter the Groq API Key")

            llm=chat_groq(api_key=groq_api_key,model_name=selected_groq_model)

        except Exception as e:
            raise ValueError(f"Error Occured with Exception :{e}")
        return llm 
