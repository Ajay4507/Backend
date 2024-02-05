from Main import Connection
Cursor=Connection.cursor()

Get="select * from Department"
Cursor.execute(Get)
Result = Cursor.fetchall()
for rec in Result:
    print(rec)