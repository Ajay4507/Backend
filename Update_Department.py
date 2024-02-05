from Main import Connection
Cursor=Connection.cursor()

Update="UPDATE Department SET Dept_Name='Deposits' WHERE Dept_Name='Cash Management'"
Cursor.execute(Update)
Connection.commit()