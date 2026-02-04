import streamlit as st
st.title("my age and city")
age = st.slider("Enter your age:",1,100)
city = st.selectbox("Select your city:",["New York","Los Angeles","Chicago","Houston","Phoenix"])

if st.button("Show the details"):

    st.write("Your age is", age, "and you live in", city)

