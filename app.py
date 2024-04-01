# Bring in deps
import os
from apikey import apikey

import streamlit as st
from langchain.llms import openai

os.environ['OPENAI_API_KEY'] = apikey

#A App framework
st.title('✨ Youtube GPT Creator')
prompt = st.text_input('Plug in your prompt here')

#h

