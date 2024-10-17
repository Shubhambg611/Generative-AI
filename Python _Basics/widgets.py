import streamlit as st
st.title("test input")
name=st.text_input("Enter your name:")

if name:
    st.write("Hello {name}")