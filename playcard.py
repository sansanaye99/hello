import streamlit as st
import test
a=st.text_input("please enter your name")
b=st.text_input("please enter your age")
st.write("Your name is"+a)
st.write("Your age is"+b)
test.display(a)



