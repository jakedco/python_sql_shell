import os, pyodbc

# Database details
# This is all you need to edit.
server = r"SERVER_NAME"
database = "DATABASE_NAME"

# Command to connect to the Database and get a cursor
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';Trusted_Connection=yes')
cursor = cnxn.cursor()
cursor_input = ""

print("enter 'q!' to quit")

while cursor_input != "q!":
    cursor_input = input('$')
    if len(cursor_input) == 0:
        continue
    if cursor_input == "q!":
        break
    cursor.execute(cursor_input)
    print(cursor.fetchall())
    
