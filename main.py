import streamlit as st
from factorial import factorial

def main():
    st.title("Factorial Caculator")
    number = st.number_input("Enter a number: ",
                             min_value=0,
                             max_value=900)
    if st.button('Calculator'):
        result = factorial(number)
        st.write(f'The factorial of {number} is {result}')
        st.balloons()
    
if __name__ == '__main__':
    main()