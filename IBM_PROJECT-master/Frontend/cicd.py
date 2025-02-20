import streamlit as st

st.title("Welcome to the World!!")
input_txt = st.text_input("How can I help You...")

if input_txt:
    st.write(f"You asked: {input_txt}. I am a poet here to help!")