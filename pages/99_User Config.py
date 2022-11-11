import streamlit as st
#st.set_page_config(layout="wide")
#import streamlit_authenticator as stauth
#from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
import pandas as pd

import sys
# adding Folder_2 to the system path
sys.path.insert(0, '../')

import viewer as vw

if st.session_state["authentication_status"] == False:
    st.write("User not authenticated")

if st.session_state["authentication_status"] == "":
    st.write("User not authenticated")

if st.session_state["authentication_status"] == True:
    st.title("User Information")


    config = st.session_state["config"]

    test = pd.DataFrame.from_dict(config['credentials']['usernames'],orient='index',columns=['username','email','name','password'])
    test.drop(['password'], axis=1, inplace=True)

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

    selected = vw.grid_view(test)


    st.write(len(selected))


    if len(selected) != 0:
        #st.write(selected[0]['name'])
        st.button("Testing")
    #st.dataframe(df)