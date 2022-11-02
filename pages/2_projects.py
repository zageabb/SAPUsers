import streamlit as st
import streamlit_authenticator as stauth


if st.session_state["authentication_status"] == False:
    st.write("User not authenticated")

if st.session_state["authentication_status"] == "":
    st.write("User not authenticated")


if st.session_state["authentication_status"] == True:
    st.title("Projects")

    st.write("You have entered:", st.session_state["my_input"])