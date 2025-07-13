import streamlit as st

st.title("Power calculator")
st.write("Input a number to see its power of 2, 3 and 5")

n = st.number_input("Enter an integer", value=1, step=1)

# calculate
square = 2**n
cube = 2**n
fifth = 2**5

st.write(f"The square of {n} is {square}")
st.write(f"The cube of {n} is {cube}")
st.write(f"The fifth of {n} is {fifth}")