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


if st.session_state["authentication_status"] == False:
    st.write("User not authenticated")

if st.session_state["authentication_status"] == "":
    st.write("User not authenticated")


if st.session_state["authentication_status"] == True:

    question = st.text_input("Question to ask:") #, st.session_state["TCode_search"]
    submit = st.button("Submit")

    if submit:

        Sql_question = f"INSERT INTO Questions(Question) \
            VALUES ('{question}');"

        Question_Submit = engine.execute(Sql_question)
        st.text_input = ""
        Question_Submit.close()

    st.write("Questions:")

            
    Sql_code = f"SELECT Question, Answered \
            FROM Questions;"
            #WHERE (((S4_Roles_Tcodes.Tcode_App) LIKE '%{search}%'));"

    #st.write(Sql_code)

    Question_List = engine.execute(Sql_code)
            

    Questions = pd.DataFrame(Question_List,columns=['Question', 'Answered'])
    Questions_Selected = vw.grid_view(Questions)
    Question_List.close()