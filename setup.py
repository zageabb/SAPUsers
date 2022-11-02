import streamlit as st
import streamlit_authenticator as stauth
import yaml

with open('./config.yaml') as file:
    config = yaml.safe_load(file)

hashed_passwords = stauth.Hasher(['123', '456']).generate()

print(hashed_passwords)
#authenticator = stauth.Authenticate(
#    config['credentials'],
#    config['cookie']['name'],
#    config['cookie']['key'],
#    config['cookie']['expiry_days'],
#    config['preauthorized']
#)

#name, authentication_status, username = authenticator.login('Login', 'main')

#if authentication_status:
#    authenticator.logout('Logout', 'main')
#    st.write(f'Welcome *{name}*')
#    st.title('Some content')
#elif authentication_status == False:
#    st.error('Username/password is incorrect')
#elif authentication_status == None:
#    st.warning('Please enter your username and password')