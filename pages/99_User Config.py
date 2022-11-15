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

    Sql_code1 = f"SELECT username, name, email, pwd \
        FROM users;" # \
        #WHERE (User_Name='{username}');"

    users = engine.execute(Sql_code1)
        

    Users = pd.DataFrame(users,columns=['User Name','Name', 'Email', 'PWD'])
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

    if len(Users_Selected) != 0:
        st.write("User selected: ", Users_Selected[0]['Name'])
        left, centre, right = st.columns(3)
        with left:
            add_user = st.button('Add User')

        with centre:
            update_user = st.button('Update User')

        with right:
            delete_user = st.button('Delete User')

        reset = st.button('Reset Password')

        if add_user:
            with st.form("User Add"):
                UserName = st.text_input("UserName")
                Name = st.text_input("Name")
                Email = st.text_input("Email")
                Pwd = st.text_input("Password")

                submit = st.form_submit_button("Submit")

                if submit:
                    pwd = stauth.Hasher(Pwd).generate()

                    sql_code2 = f"INSERT INTO users(username, name, email, pwd)  \
                        VALUES ('{UserName}','{Name}','{Email}','{pwd}',1);"
                    st.write(sql_code2)
                    UserAdded = engine.execute(sql_code2)
                    st.success('User Added')  
                    UserAdded.close()







    #st.dataframe(df)