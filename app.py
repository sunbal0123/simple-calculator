import streamlit as st

# Title for the Streamlit app
st.title("Simple Calculator")

# Input for the first number
num1 = st.number_input("Enter the first number:", value=0.0)

# Select the operation
operation = st.selectbox("Choose the operation:", ("+", "-", "*", "/"))

# Input for the second number
num2 = st.number_input("Enter the second number:", value=0.0)

# Button to calculate the result
if st.button("Calculate"):
    if operation == '+':
        result = num1 + num2
        st.write(f"Result: {num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        st.write(f"Result: {num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        st.write(f"Result: {num1} * {num2} = {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            st.write(f"Result: {num1} / {num2} = {result}")
        else:
            st.error("Error! Division by zero.")
