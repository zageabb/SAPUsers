import streamlit as st
#import streamlit_authenticator as stauth
#st.set_page_config(layout="wide")
import sys
# adding Folder_2 to the system path
sys.path.insert(0, '../')
from database import *
import viewer as vw

import pandas as pd
import time as tt

#from sqlalchemy import create_engine
import sqlalchemy as sa

if st.session_state["authentication_status"] == False:
    st.write("User not authenticated")

if st.session_state["authentication_status"] == "":
    st.write("User not authenticated")


if st.session_state["authentication_status"] == True:
    st.write("S4 Copy Profile")



    #st.write("You have entered:", st.session_state["my_input"])

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("Copy from user")
        #st.image("https://static.streamlit.io/examples/cat.jpg")

        result = engine.execute(
        
            "SELECT Full_Name,User_Name, User_Master, Complete, Exclude \
            FROM Legacy_Users;"
        )

        test = pd.DataFrame(result,columns=['Full Name','User Name','User Master','Complete', 'Exclude'])
        #test.drop(['password'], axis=1, inplace=True)
    
        #st.write("User Selection")
        selected = vw.grid_view(test)
        result.close()
        #st.write(len(selected))

        st.write('Legacy Role Filter')

        Sql_code = f"SELECT DISTINCT Legacy_User_Role.Role, Legacy_Roles.Stream, Legacy_User_Role.Active \
            FROM Legacy_User_Role INNER JOIN Legacy_Roles ON Legacy_User_Role.Role = Legacy_Roles.Role \
            WHERE ((Legacy_Roles.Block)='False');"

        LegacyRoles = engine.execute(Sql_code)
        

        Roles = pd.DataFrame(LegacyRoles,columns=['Role', 'Stream','Active'])
        LRoles_Selected = vw.grid_view(Roles)
        LegacyRoles.close() 


    with col2:
        st.write("Copy to user")
        #st.image("https://static.streamlit.io/examples/dog.jpg")

        if len(LRoles_Selected) !=0:
            
            LRole = (LRoles_Selected[0]['Role'])

            result2 = engine.execute(
        
                f"SELECT Legacy_Users.User_Name, Legacy_Users.Full_Name, Legacy_Users.User_Master, Legacy_Users.Complete, Legacy_Users.Exclude \
                FROM Legacy_Users INNER JOIN Legacy_User_Role ON Legacy_Users.User_Name = Legacy_User_Role.User_Name \
                WHERE (((Legacy_User_Role.Role)='{LRole}') AND (Legacy_Users.Complete='False'));"
            )

            test2 = pd.DataFrame(result2,columns=['User Name','Full Name','User Master','Complete', 'Exclude'])
            #test.drop(['password'], axis=1, inplace=True)
    
            #st.write("User Selection")
            selected2 = vw.grid_view(test2,'multi')
            #st.write(len(selected))
            result2.close()

    with col3:
        st.write('Actions')
        if len(LRoles_Selected) !=0 and len(selected) !=0 and len(selected2) !=0:
            new_profile = st.button('Add S4 profile')
            close_profile = st.button('Close S4 profile')
            max_users = len(selected2)
            if new_profile:
                for x in range(max_users):
                    st.write('adding profile to: ', selected2[x]['User Name'])

                    add_roles = engine.execute(

                    f"INSERT INTO S4_User_Role ( User_Name, Role, E2E_stream ) \
                    SELECT '{selected2[x]['User Name']}' AS [username], S4_User_Role.Role, S4_User_Role.E2E_stream \
                    FROM S4_User_Role \
                    WHERE (((S4_User_Role.User_Name)='{selected[0]['User Name']}'));"

                    )

                    add_roles.close()
                    #tt.sleep(0.5)
            
            if close_profile:
                for x in range(max_users):
                    st.write('Closing profile to: ', selected2[x]['User Name'])

                    add_roles = engine.execute(

                    f"UPDATE Legacy_Users SET Legacy_Users.Complete = 'True' \
                        WHERE (((Legacy_Users.User_Name)='{selected2[x]['User Name']}'));"

                    )
                    add_roles.close()

                    #tt.sleep(0.5)

