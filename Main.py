import os
import streamlit as st
import pandas as pd

@st.dialog("Result ")
def pop_up(message: str):
    st.write(message)
    if st.button("Close"):
        st.rerun()


file_name = 'ErrorCodes.csv'

if 'error_codes' not in st.session_state:
    st.session_state['error_codes'] = pd.read_csv(file_name)

error_codes_input = st.chat_input('Enter error codes separated by a comma')

if error_codes_input:
    error_codes = error_codes_input.split(',')

    if len(error_codes) == 1:
        df_errors = st.session_state['error_codes']
        df_result = df_errors[df_errors['Code'] == int(error_codes[0])]

        if df_result.empty:
            # st.subheader(f'Code {error_codes[0]} not found')
            pop_up(f'Code {error_codes[0]} not found')
        else:
            description = df_result['Description'].iloc[0]
            # st.subheader(f'{error_codes[0]}: {description}')
            pop_up(f'{error_codes[0]}: {description}')

st.dataframe(st.session_state['error_codes'])
