from Main import mydb
cur=mydb.cursor()

select ="select * from Employee"
cur.execute(select)
result = cur.fetchall()
for rec in result:
    print(rec)
