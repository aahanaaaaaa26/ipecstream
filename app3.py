import streamlit as st
st.title("basic calculator")
num1 = st.number_input("Enter first number:")
num2 = st.number_input("Enter second number:")
operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
    if operation == "Add":
        st.write("The result is:", num1 + num2)
    elif operation == "Subtract":
        st.write("The result is:", num1 - num2)
    elif operation == "Multiply":
        st.write("The result is:", num1 * num2)
    elif operation == "Divide":
        if num2 != 0:
            st.write("The result is:", num1 / num2)
        else:
            st.write("Error: Division by zero")