#import pickle
#from pathlib import Path
#from nbformat import from_dict
import streamlit as st
st.set_page_config(layout="wide",
    page_title="Gerry's SAP Roles App"
    )
import streamlit_authenticator as stauth
#import yaml
import json
import numpy as np
import pandas as pd
#import sqlalchemy as sa
#import sys 
#import os
#sys.path.append(os.path.abspath("./pages/database.py"))
from database import *
import viewer as vw
import User_Dict as ud


#from .authenticate import Authenticate


#st.set_page_config(
#    page_title="Gerry's SAP Roles App",
    
#)

#connection_accdb = (
#    r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
#    r"DBQ=.\SAPRoles.accdb;"
#    r"ExtendedAnsiSQL=1;"
#)

#connection_url = sa.engine.URL.create(
#    "access+pyodbc",
#    query={"odbc_connect": connection_accdb}
#)
#engine = sa.create_engine(connection_url)

#with open('./config.yaml') as file:
#    config = yaml.safe_load(file)

with open("./config.json") as file:
    config = json.load(file)

sql_code1 = f"SELECT username, email, name, pwd, force \
    FROM users;" # \
    #WHERE (username ='{edituser}');"

users = engine.execute(sql_code1)
Users = pd.DataFrame(users,columns=['username','email','name', 'pwd', 'force']) #, index=None
#vw.grid_view(Users)
users.close() 
creda = ud.userdict(Users)

#creds = Users['username'].to_dict()
    
    
#st.write(creda)
#st.write(config['credentials'])

authenticator = stauth.Authenticate(creda, config['cookie']['name'], config['cookie']['key'], cookie_expiry_days=config['cookie']['expiry_days'])
#authenticator = stauth.Authenticate(
#    config['credentials'],
#    config['cookie']['name'],
#    config['cookie']['key'],
#    config['cookie']['expiry_days'],
#    config['preauthorized']
#)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status: # True login
    authenticator.logout('Logout', 'sidebar')

    CurrentUser=Users.loc[Users['username'] == f'{username}']

    mask = Users['username'] == f'{username}'
    pos = int(np.flatnonzero(mask))

    #st.session_state["name"] = name
    #st.session_state["authentication_status"]=authentication_status


    st.title("Main Page")
    
    st.write(f'Welcome *{name}*')
    #st.title('Some content')
    st.write("You're now logged into the SAP Roles App. Select pages on the left sidebar to use those facitilites")

    st.write(pos)

    if CurrentUser['force'][pos]==-1:
        NewPassword = st.text_input("Enter new password")
        Update = st.button('Update Password')

        if Update:
            st.write(NewPassword)
            Pwd = stauth.Hasher([NewPassword]).generate()
            st.write(Pwd)
            Sql_code6 = f"UPDATE users \
                SET pwd = '{Pwd[0]}', force=0 \
                WHERE (username='{username}');" #.format(pwd = chr(34) + str(Pwd) + chr(34), user = username)
            
            passUpdated = engine.execute(Sql_code6)
            st.success('User password set')  
            passUpdated.close()

            #rnd = [str(random.randint(1000,9999))]
            #st.write("New password generated: ",rnd)
            #pwd = stauth.Hasher(rnd).generate()
            #Sql_code6 = f"UPDATE users \
            #    SET pwd = '{pwd[0]}', force=-1 \
            #    WHERE (username='{Users_Selected[0]['User Name']}');"
            
            #UserAdded = engine.execute(Sql_code6)
            #st.success('User Reset')  
            #UserAdded.close()            

    #st.write(config['credentials'])
    #st.write(config['cookie']['name'])
    #st.write(config['cookie']['key'])
    #st.write(config['cookie']['expiry_days'])
    #st.write(config['preauthorized'])

   # st.sidebar.success("Select a page above")

    #if "engine" not in st.session_state:
    #    st.session_state["engine"] = engine


    #if "my_input" not in st.session_state:
    #    st.session_state["my_input"] = ""

    #my_input = st.text_input("Input a text here", st.session_state["my_input"])
    #submit = st.button("Submit")

    #if submit:
    #    st.session_state["my_input"] = my_input
    #    st.write("You have entered:", my_input)

    if "config" not in st.session_state:
        st.session_state["config"] = "database" #creda #config



elif authentication_status == False:
    st.error('Username/password is incorrect')

elif authentication_status == None:
    st.warning('Please enter your username and password')





