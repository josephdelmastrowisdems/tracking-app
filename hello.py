import streamlit as st

st.write("Hello World")
x = st.text_input("Favourite movie?") 
st.write(f"Your favorite movie is {x}")