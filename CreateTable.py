from Main import mydb

cur=mydb.cursor()

createtable="CREATE TABLE Employee (Emp_id int primary key, Emp_name varchar(50), Emp_salary int)"

cur.execute(createtable)