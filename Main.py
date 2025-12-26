import os
import streamlit as st
import pandas as pd
import base64

@st.dialog("Result")
def pop_up(message: str):
    st.write(message)
    # if st.button("Close"):
    #     st.rerun()


def set_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded_string = base64.b64encode(file.read())

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string.decode()}");
            # background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


# Inject CSS to hide the header, hamburger menu, and footer
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            footer {visibility: hidden;}
            div[data-testid="stDecoration"] {display: none;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


# Call the function with your local file name
# set_bg_from_local('troubleshoot-icon-15.jpg')

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    </style>
    """,
    unsafe_allow_html=True
)

file_name = 'ErrorCodes.csv'

if 'error_codes' not in st.session_state:
    st.session_state['error_codes'] = pd.read_csv(file_name)

    df_display = st.session_state['error_codes'].copy()
    df_display = df_display[df_display['Description'] != 'Description is missing']
    df_display.sort_values(by=['Code'], inplace=True)
    df_display.reset_index(drop=True, inplace=True)
    st.session_state['df_display'] = df_display
    st.session_state['error_codes']['Code'] = st.session_state['error_codes']['Code'].astype(str)


def search_function(search_term: str) -> list:
    # Replace with your actual search logic (e.g., querying a database, API)
    # This example uses a simple static list for demonstration
    all_options = st.session_state['error_codes_list']
    return [item for item in all_options if str(search_term).lower() in str(item).lower()]



st.header('Spike LR Troubleshooting')
# error_codes_input = st.chat_input('Enter error codes separated by a comma')
error_codes_input = st.text_input('Enter error codes separated by a comma')


if error_codes_input:
    error_codes = error_codes_input.split(',')
    print(f"Error codes: {error_codes}")

    if len(error_codes) == 1:
        df_errors = st.session_state['error_codes']
        df_result = df_errors[df_errors['Code'] == error_codes[0]]

        if df_result.empty:
            # st.subheader(f'Code {error_codes[0]} not found')
            pop_up(f'Code {error_codes[0]} not found')
        else:
            description = df_result['Description'].iloc[0]
            # st.subheader(f'{error_codes[0]}: {description}')
            pop_up(f'{error_codes[0]}: {description}')


st.write(st.session_state['df_display'].style.hide(axis="index").to_html(), unsafe_allow_html=True)
