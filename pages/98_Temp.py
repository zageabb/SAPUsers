import streamlit as st
#st.set_page_config(layout="wide")
import streamlit_authenticator as stauth
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
import pandas as pd
import random

import sys
# adding Folder_2 to the system path
sys.path.insert(0, '../')
from database import *

import viewer as vw


#if st.session_state["authentication_status"] == False:
#    st.write("User not authenticated")

#if st.session_state["authentication_status"] == "":
#    st.write("User not authenticated")

#if st.session_state["authentication_status"] == True and st.session_state['username']=='gaabbot':
#if st.session_state["authentication_status"] == False:
    st.title("User Information")

    config = st.session_state["config"]
    name = st.session_state["username"]

    Sql_code1 = f"SELECT username, name, email, pwd, force \
        FROM users;" # \
        #WHERE (User_Name='{username}');"

    users = engine.execute(Sql_code1)
        

    Users = pd.DataFrame(users,columns=['User Name','Name', 'Email', 'PWD','Force'])
    Users_Selected = vw.grid_view(Users)
    users.close()

    config = st.session_state["config"]

    #test = pd.DataFrame.from_dict(config['credentials']['usernames'],orient='index',columns=['username','email','name','password'])
    #test.drop(['password'], axis=1, inplace=True)

    #grid_response = AgGrid(test,reload_data=True)

    #gb = GridOptionsBuilder.from_dataframe(test)
    #gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
    #gb.configure_side_bar() #Add a sidebar
    #gb.configure_selection('single', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
    #gridOptions = gb.build()

    #st.dataframe(test)
    #grid_response = AgGrid(
    #    test,
    #    gridOptions=gridOptions,
    #    data_return_mode='AS_INPUT', 
    #    update_mode='MODEL_CHANGED', 
    #    fit_columns_on_grid_load=False,
    #    theme='streamlit', #Add theme color to the table
    #    enable_enterprise_modules=True,
    #    height=350, 
    #    width='100%',
    #    reload_data=False
    #)

    #data = grid_response['test']
    #selected = grid_response['selected_rows']
    #df = pd.DataFrame(selected)

   # selected = vw.grid_view(test)

    st.write(len(Users_Selected))
    st.session_state["edituser"] = ""
    if len(Users_Selected) != 0:
        st.write("User selected: ", Users_Selected[0]['Name'])
        st.session_state["edituser"] = Users_Selected[0]['User Name']
        #left, centre, right = st.columns(3)
        #with left:
        #    add_user = st.button('Add User')

        #with centre:
        #    update_user = st.button('Update User')

        #with right:
        #    delete_user = st.button('Delete User')

        reset = st.button('Reset Password')

        if reset:
            rnd = [str(random.randint(1000,9999))]
            st.write("New password generated: ",rnd)
            pwd = stauth.Hasher(rnd).generate()
            Sql_code6 = f"UPDATE users \
                SET pwd = '{pwd[0]}', force=-1 \
                WHERE (username='{Users_Selected[0]['User Name']}');"
            
            UserAdded = engine.execute(Sql_code6)
            st.success('User Reset')  
            UserAdded.close()

        #if "sql2" in st.session_state: 
        #    sql_code2 = st.session_state["sql2"]
        #else:
        #    sql_code2 = ""

        #if add_user:


        #    frm = st.form("User Add")#:
        #   UserName = frm.text_input("UserName")
        #    Name = frm.text_input("Name")
        #    Email = frm.text_input("Email")
        #    Pwd = frm.text_input("Password")

        #    submit = frm.form_submit_button("Add")

        #    if submit:
        #        pwd = Pwd #stauth.Hasher(Pwd).generate()
        #        sql_code2 = f"INSERT INTO users(username, name, email, pwd, force)  \
        #            VALUES ('{UserName}','{Name}','{Email}','{pwd}',0);"
        #        st.session_state["sql2"]= sql_code2
                    #UserAdded = engine.execute(sql_code2)
                    #st.success('User Added')  
                    #UserAdded.close()


        #st.write("sql2:",sql_code2)




    #st.dataframe(df)
