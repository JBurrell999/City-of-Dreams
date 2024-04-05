from dotenv import load_dotenv
import os
import streamlit as st
import pandasai.pandas as pd
from pandasai import SmartDataframe
from pandasai.llm.openai import OpenAI
import matplotlib

matplotlib.use('Agg')

load_dotenv()

API_KEY = os.environ.get('OPENAI_API_KEY', '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')

os.environ['PANDASAI_API_KEY'] = '$2a$10$LcxR6H.NbnF2nY/yuW7N3OuwP8KUnejwFRd7rfL8KXi.CWK2EY4h'

llm = OpenAI(api_token=API_KEY)

st.title("Data Analysis for City of Dreams")
uploaded_file = st.file_uploader("Upload a csv file for analysis", type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head(10))

    try:
        pandas_ai = SmartDataframe(df)
        prompt = st.text_area("Enter Prompt:")
        
        if st.button("Generate"):
            if prompt:
                with st.spinner("City of Dream's Analysis Tool is generating an answer, please wait"):
                    # Adjusted call to chat method without using keyword argument for prompt
                    result = pandas_ai.chat(prompt)
                    st.write(result)
            else:
                st.warning("Please enter a prompt.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
