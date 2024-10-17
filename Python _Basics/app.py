import streamlit as st
import pandas as pd
import numpy as np 


st.title("Hello shubham") #Title

st.write("Simple test")

#simple dataframe
df = pd.DataFrame({
    'first column':[1,2,3,4],
    'Second Column':[10,20,30,40]
})

st.write("Here is DF")
st.write(df)

#create a line chart 
chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)


st.title("text input")
name=st.text_input("Enter your name:")

if name:
    st.write(f"Hello {name}") 
    
    
#slider
age = st.slider("select your age",0,100,25)
st.write(f"your age is {age}")


options = ["Python","java","C++","JS"]
choice = st.selectbox("choose ur fav lang",options)
st.write(f"You selected {choice}")