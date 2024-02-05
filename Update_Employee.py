from Main import mydb
cur=mydb.cursor()

update="UPDATE Employee SET Emp_salary=Emp_salary+5000 WHERE Emp_id=2"

cur.execute(update)

mydb.commit()