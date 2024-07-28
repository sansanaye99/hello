import streamlit as st
import test
a=st.text_input("please enter your name")
b=st.text_input("please enter your age")
if (b<=18):
  st.write("you are not allow to access the site")
else:
  st.write("You are eligible to play the game")
  st.write("Your name is"+a)
  st.write("Your age is"+b)
  test.display(a)



