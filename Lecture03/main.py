

import streamlit as st

import pywhatkit as kit
import pandas as pd

import pyautogui
import time


st.set_page_config("WhatsApp Automation Tool", page_icon="📱")

st.title("WhatsApp Automation Tool ")
st.write("WhatsApp pr message send hongy ")

meriuploadFile= st.file_uploader("upload an excel file ",type=["xlsx"]) 

portfolio=st.text_input("Enter Your Portfolio", value="https://syedmuhammadarsalanshah.vercel.app/")
customMessage=st.text_area("Enter Your Complete Detail Msg", value="Follow me")

if meriuploadFile is not None:
    df=pd.read_excel(meriuploadFile)
    st.dataframe(df)
    if st.button("send message"):
        try:
            for i ,row in df.iterrows():
                phoneNumber=f"+{row["Phone"]}"
                message=f"{customMessage},{portfolio}"
                kit.sendwhatmsg_instantly(phoneNumber,message,wait_time=30)
                time.sleep(8)
                pyautogui.press("enter")
                st.write("sent message")
                time.sleep(5)
                pyautogui.press("enter")
        except Exception as e:
            st.write(e)
