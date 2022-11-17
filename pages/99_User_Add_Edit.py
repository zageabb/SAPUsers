import streamlit as st
#st.set_page_config(layout="wide")
import streamlit_authenticator as stauth
#from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
import pandas as pd

import sys
# adding Folder_2 to the system path
sys.path.insert(0, '../')
from database import *

import viewer as vw


if st.session_state["authentication_status"] == False:
    st.write("User not authenticated")

if st.session_state["authentication_status"] == "":
    st.write("User not authenticated")

if st.session_state["authentication_status"] == True:
    st.title("User Information")

    config = st.session_state["config"]
    name = st.session_state["username"]

    if "edituser" in st.session_state:
        edituser = st.session_state["edituser"]

        if edituser !="":
            st.write("Edit User")

            sql_code1 = f"SELECT username, name, email, pwd \
                FROM users \
                WHERE (username ='{edituser}');"

            existinguser = engine.execute(sql_code1)
            Existing_User = pd.DataFrame(existinguser,columns=['User Name','Name', 'Email','Pwd'])
            #LRoles_Selected = vw.grid_view(Roles)
            existinguser.close()   
        else:
            st.write("Add User")     


    else:
        edituser = ""
    

    if edituser =="":
        frm = st.form("User Add/Edit")#:
        UserName = frm.text_input("UserName")
        Name = frm.text_input("Name")
        Email = frm.text_input("Email")
        Pwd = frm.text_input("Password")
    else:
        frm = st.form("User Add/Edit")#:
        UserName = frm.text_input("UserName")
        Name = frm.text_input("Name")
        Email = frm.text_input("Email")
        #Pwd = frm.text_input("Password")

    if edituser =="":
        submit = frm.form_submit_button("Add")
    else:
        submit = frm.form_submit_button("Update")

    if submit:
        pwd = Pwd #stauth.Hasher(Pwd).generate()
        sql_code2 = f"INSERT INTO users(username, name, email, pwd, force)  \
            VALUES ('{UserName}','{Name}','{Email}','{pwd}',0);"
        UserAdded = engine.execute(sql_code2)
        st.success('User Added/Updated')  
        UserAdded.close()




    #st.dataframe(df)