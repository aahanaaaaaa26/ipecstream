import streamlit as st
st.title("Hello, Streamlit!")
name = st.text_input("Enter your name:")
if st.button("Greet me!"):
    st.write("hello", name)