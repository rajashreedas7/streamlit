import streamlit as st

def largest_of_three_numbers(num1, num2, num3):
    largest = num1
    if num2 > largest:
        largest = num2
    if num3 > largest:
        largest = num3
    return largest

st.title("Find the largest among 3 numbers")

num1 = st.number_input("Enter the first number", value=0, step=1)
num2 = st.number_input("Enter the second number", value=0, step=1)
num3 = st.number_input("Enter the third number", value=0, step=1)

if st.button("Find the largest"):
    result = largest_of_three_numbers(num1, num2, num3)
    st.write(f"The largest number is {result}")
