import streamlit as st
#st.set_page_config(layout="wide")
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

if "user_complete" not in st.session_state:
    st.session_state["user_complete"] = ['True','False']

user_complete = st.session_state["user_complete"]

if "user_exclude" not in st.session_state:
    st.session_state["user_exclude"] = ['True','False']

user_exclude = st.session_state["user_exclude"]

if st.session_state["authentication_status"] == False:
    st.write("User not authenticated")

if st.session_state["authentication_status"] == "":
    st.write("User not authenticated")


if st.session_state["authentication_status"] == True:
    
    comp = user_complete

    complist = ""

    for x in range(len(comp)):
        if complist == "":
            complist = f"(Complete='{comp[x]}')"
        else:
            complist = complist + f" OR (Complete='{comp[x]}')"

    excl = user_exclude

    excllist = ""

    for x in range(len(excl)):
        if excllist == "":
            excllist = f"(Exclude='{excl[x]}')"
        else:
            excllist = excllist + f" OR (Exclude='{excl[x]}')"


    #st.write("You have entered:", st.session_state["my_input"])

    user_list =f"SELECT Full_Name,User_Name, User_Master, Complete, Exclude \
            FROM Legacy_Users \
            WHERE (({complist}) AND ({excllist}));"


    result = engine.execute(user_list)

    test = pd.DataFrame(result,columns=['Full Name','User Name','User Master','Complete', 'Exclude'])
    #test.drop(['password'], axis=1, inplace=True)
    with st.sidebar:
        st.write("User Selection")
        selected = vw.grid_view(test)
        st.write(len(selected))

        st.write()
        user_complete = st.multiselect(
            "Complete ?",
            options=['True','False'],
            help = 'Legacy user field complete',
            default = st.session_state["user_complete"]
        )
        user_exclude = st.multiselect(
            "Exclude ?",
            options=['True','False'],
            help = 'Legacy user field exclude',
            default = st.session_state["user_exclude"]
        )

        if user_complete:
            st.session_state["user_complete"] = user_complete

        if user_exclude:
            st.session_state["user_exclude"] = user_exclude



    


    if len(selected) != 0:
        st.write(selected[0]['Full Name'])
        User_Name = selected[0]['User Name']
        
        st.write('S4 Roles')
        #Sql_code = f"SELECT User_Name, Role, Start_date, End_date, Active FROM Legacy_User_Role WHERE (User_Name = '{User_Name}');"

        Sql_code1 = f"SELECT User_Name, Role, E2E_stream \
            FROM S4_User_Role \
            WHERE (User_Name='{User_Name}');"

        S4Roles = engine.execute(Sql_code1)
        

        Roles = pd.DataFrame(S4Roles,columns=['User Name','Role', 'Stream'])
        S4Roles_Selected = vw.grid_view(Roles)
        S4Roles.close()
        if len(S4Roles_Selected) !=0:
            remove_role = st.button("Remove Role from User")

            if remove_role:
                S4Role = (S4Roles_Selected[0]['Role'])

                Sql_code5 = f"DELETE * \
                    FROM S4_User_Role \
                    WHERE ((User_Name='{User_Name}') AND (Role='{S4Role}'));"

                    
                    
                Roles_removal = engine.execute(Sql_code5)
                st.success('Role removed from user')
                Roles_removal.close()

        Sql_code2 = f"SELECT S4_Roles.E2E_stream \
                        FROM S4_Roles \
                        GROUP BY S4_Roles.E2E_stream \
                        ORDER BY S4_Roles.E2E_stream;"

        S4Roles_List = engine.execute(Sql_code2)

        S4_Roles = pd.DataFrame(S4Roles_List, columns=['S4 Roles'])
        S4Roles_List.close()
        platform_name = st.selectbox ('Stream',options= S4_Roles)

        st.write(platform_name)

        if platform_name != "":

            Sql_code3 = f"SELECT S4_Roles.E2E_stream, S4_Roles.Business_Role_Name, S4_Roles.Description \
                    FROM S4_Roles \
                    WHERE (((S4_Roles.E2E_stream)='{platform_name}'));"
                    
            Roles_List = engine.execute(Sql_code3) 
            Roles_filtered = pd.DataFrame(Roles_List, columns=['E2E Stream','Business Role Name','Description'])  
            S4filtered_Selected = vw.grid_view(Roles_filtered)
            Roles_List.close()
        if len(S4filtered_Selected) != 0:
            copy_role = st.button("Copy Role to User")

            if copy_role:
                #st.write(User_Name)
                busRole = (S4filtered_Selected[0]['Business Role Name'])
                Desc =  (S4filtered_Selected[0]['Description'])

                Sql_code4 = f"INSERT INTO S4_User_Role (User_Name, Role, E2E_stream) \
                    VALUES ('{User_Name}','{busRole}','{Desc}');"
                    
                    
                Roles_List = engine.execute(Sql_code4)
                st.success('Role added to user')
                Roles_List.close()

        st.write('Legacy Roles')
        #Sql_code = f"SELECT User_Name, Role, Start_date, End_date, Active FROM Legacy_User_Role WHERE (User_Name = '{User_Name}');"

        Sql_code = f"SELECT Legacy_User_Role.User_Name, Legacy_User_Role.Role, Legacy_Roles.Stream, Legacy_User_Role.Start_date, Legacy_User_Role.End_date, Legacy_User_Role.Active \
            FROM Legacy_User_Role INNER JOIN Legacy_Roles ON Legacy_User_Role.Role = Legacy_Roles.Role \
            WHERE (((Legacy_User_Role.User_Name)='{User_Name}') AND ((Legacy_Roles.Block)='False'));"

        LegacyRoles = engine.execute(Sql_code)
        

        Roles = pd.DataFrame(LegacyRoles,columns=['User Name','Role', 'Stream','Start Date', 'End Date','Active'])
        LRoles_Selected = vw.grid_view(Roles)
        LegacyRoles.close()
        complete = st.button('Mark User Complete')

        if complete:
            Sql_code6 = f"UPDATE Legacy_Users \
                SET Complete = 'True' \
                WHERE (User_Name='{User_Name}');"

            UserComplete = engine.execute(Sql_code6)
            st.success('User Updated')  
            UserComplete.close()    
    #st.dataframe(df)

        uncomplete = st.button('Mark User Open')

        if uncomplete:
            Sql_code7 = f"UPDATE Legacy_Users \
                SET Complete = 'False' \
                WHERE (User_Name='{User_Name}');"

            UserUnComplete = engine.execute(Sql_code7)
            st.success('User Updated')  
            UserUnComplete.close()  
