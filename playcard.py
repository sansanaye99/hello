import streamlit as st
import test
a=st.text_input("please enter your name")
b= st.number_input('second', min_value=0, max_value=100, value=0, step=1)
if(b<=18):
  st.write("you are not allow to access the site")
else:
  st.write("You are eligible to play the game")
  st.write("Your name is"+a)
  st.write("Your age is ",b)
  test.display(a)



