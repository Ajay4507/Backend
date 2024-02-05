from Main import mydb
import mysql.connector
cur = mydb.cursor()

insert="INSERT INTO Employee (Emp_id,Emp_name,Emp_salary) VALUES(%s,%s,%s)"
details=[(1,'Alex',35000),(2,'Steven',30000),(3,'John',40000),(4,'Nancy',37000),(5,'Daina',41000)]
cur.executemany(insert,details)
mydb.commit()

