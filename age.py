import streamlit as st
import datetime as datetime

dob=st.date_input('Enter DOB')


def Age_Calculator():
    today=datetime.datetime.now().date()
    age= int((today-dob).days/365.25)
    st.write("Your Current Age")
    st.success(age)


if st.button('Submit'):
    Age_Calculator()    

