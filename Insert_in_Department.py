from Main import Connection
import mysql.connector
Cursor=Connection.cursor()

Insertion="INSERT INTO Department (Dept_id, Dept_Name) VALUES(%s,%s)"
Values=[(1,'Cash Management'),(2,'Loan Officer'),(3,'Inspection Department'),(4,'Treasury'),(5,'Account Manager')]
Cursor.executemany(Insertion,Values)
Connection.commit()