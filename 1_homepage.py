#import pickle
#from pathlib import Path
import streamlit as st
import streamlit_authenticator as stauth
import yaml
import json

#from .authenticate import Authenticate


st.set_page_config(
    page_title="Gerry's Multipage App",
    
)


#with open('./config.yaml') as file:
#    config = yaml.safe_load(file)

with open("./config.json") as file:
    config = json.load(file)


authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status: # True login
    authenticator.logout('Logout', 'sidebar')
    st.write(f'Welcome *{name}*')
    st.title('Some content')
    st.write("You're now logged into Gerry's App. Select pages on the left sidebar to use those facitilites")

    st.title("Main Page")

   # st.sidebar.success("Select a page above")

    if "my_input" not in st.session_state:
        st.session_state["my_input"] = ""

    my_input = st.text_input("Input a text here", st.session_state["my_input"])
    submit = st.button("Submit")

    if submit:
        st.session_state["my_input"] = my_input
        st.write("You have entered:", my_input)

    if "config" not in st.session_state:
        st.session_state["config"] = config



elif authentication_status == False:
    st.error('Username/password is incorrect')

elif authentication_status == None:
    st.warning('Please enter your username and password')





