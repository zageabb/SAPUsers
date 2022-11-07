import streamlit as st
#import streamlit_authenticator as stauth

import sys
# adding Folder_2 to the system path
sys.path.insert(0, '../')
from database import *
import viewer as vw

import pandas as pd

#from sqlalchemy import create_engine
import sqlalchemy as sa


#engine = create_engine("access+pyodbc://@SAPRoles")



if st.session_state["authentication_status"] == False:
    st.write("User not authenticated")

if st.session_state["authentication_status"] == "":
    st.write("User not authenticated")


if st.session_state["authentication_status"] == True:
    
    

    #if "TCode_search" not in st.session_state:
    #    st.session_state["TCode_search"] = ""
    platform_name = st.selectbox ('Stream',options= ['Tcode','Role'])

    search = st.text_input(f"Input a {platform_name} here") #, st.session_state["TCode_search"]
    submit = st.button("Submit")

    if submit:
        if platform_name=='Tcode':
            #st.session_state["TCode_search"] = TCode_search
            st.write("S4 Roles:")

            
            Sql_code = f"SELECT E2E_stream, Business_Role_Name, Tcode_App, Description, Application \
                FROM S4_Roles_Tcodes \
                WHERE (((S4_Roles_Tcodes.Tcode_App) LIKE '%{search}%'));"

            #st.write(Sql_code)

            TCode_List = engine.execute(Sql_code)
            

            Roles = pd.DataFrame(TCode_List,columns=['E2E Stream','Business Role Name', 'Tcode/App','Description','Application'])
            LRoles_Selected = vw.grid_view(Roles)


            st.write("Legacy Roles:")
            Sql_code1 = f"SELECT Role, Tcode, Tcode_Description \
                FROM Legacy_Tcodes \
                WHERE ((Legacy_Tcodes.Tcode) LIKE '%{search}%');"


            Legacy_TCode_List = engine.execute(Sql_code1)
            

            LRoles = pd.DataFrame(Legacy_TCode_List,columns=['Role', 'Tcode','Description'])
            LegacyRoles_Selected = vw.grid_view(LRoles)

        if platform_name =='Role':
            st.write("S4 Roles:")

            
            Sql_code = f"SELECT E2E_stream, Business_Role_Name, Tcode_App, Description, Application \
                FROM S4_Roles_Tcodes \
                WHERE (((S4_Roles_Tcodes.Business_Role_Name) LIKE '%{search}%'));"

            #st.write(Sql_code)

            TCode_List = engine.execute(Sql_code)
            

            Roles = pd.DataFrame(TCode_List,columns=['E2E Stream','Business Role Name', 'Tcode/App','Description','Application'])
            LRoles_Selected = vw.grid_view(Roles)


            st.write("Legacy Roles:")
            Sql_code1 = f"SELECT Role, Tcode, Tcode_Description \
                FROM Legacy_Tcodes \
                WHERE ((Legacy_Tcodes.Role) LIKE '%{search}%');"


            Legacy_TCode_List = engine.execute(Sql_code1)
            

            LRoles = pd.DataFrame(Legacy_TCode_List,columns=['Role', 'Tcode','Description'])
            LegacyRoles_Selected = vw.grid_view(LRoles)

