from Main import Connection
Cursor=Connection.cursor()
Create_Table="CREATE TABLE Department (Dept_id int primary key, Dept_Name varchar(30))"
Cursor.execute(Create_Table)