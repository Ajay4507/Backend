import mysql.connector

class Insert:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Ajay@2002',
            database='Bank'
        )

    def insert_employee_record(self, emp_id, emp_name, emp_salary):
        cursor = self.connection.cursor()
        insert_query = "INSERT INTO Employee (Emp_id, Emp_name, Emp_salary) VALUES (%s, %s, %s)"
        record_data = (emp_id, emp_name, emp_salary)
        cursor.execute(insert_query, record_data)
        self.connection.commit()
        print("Record is Inserted....")

    def close_connection(self):
        self.connection.close()

def main():
    db_manager = Insert()

    emp_id = int(input("Enter Employee Id: "))
    emp_name = input("Enter Employee Name: ")
    emp_salary = int(input("Enter Employee Salary: "))

    db_manager.insert_employee_record(emp_id, emp_name, emp_salary)

    db_manager.close_connection()

if __name__ == "__main__":
    main()
