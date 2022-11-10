import sqlalchemy as sa

#connection_accdb = (
#    r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
#    r"DBQ=.\SAPRoles.accdb;"
#    r"ExtendedAnsiSQL=1;"
#)

connection_url =(
    f'sqlite:///SAPRoles.sqlite'
)

#connection_url = sa.engine.URL.create(
#    "access+pyodbc",
#    query={"odbc_connect": connection_accdb}
#)
engine = sa.create_engine(connection_url)