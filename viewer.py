from sqlalchemy import false
import streamlit as st
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

    #grid_response = AgGrid(test,reload_data=True)


def grid_view(data,multi='single'):
    gb = GridOptionsBuilder.from_dataframe(data)
    gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
    gb.configure_side_bar() #Add a sidebar
    #gb.configure_column()
    if multi !='single':
        gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
    else:
        gb.configure_selection('single', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
    gridOptions = gb.build()

    #st.dataframe(test)
    grid_response = AgGrid(
        data,
        gridOptions=gridOptions,
        data_return_mode='AS_INPUT', 
        update_mode='MODEL_CHANGED', 
        fit_columns_on_grid_load=False,
        theme='streamlit', #Add theme color to the table
        enable_enterprise_modules=False,
        height=350, 
        width='100%',
        reload_data=False
    )

    #data = grid_response['test']
    selected = grid_response['selected_rows']
    #df = pd.DataFrame(selected)
    #st.write(len(selected))

    return(selected)