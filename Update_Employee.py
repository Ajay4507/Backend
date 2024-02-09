import mysql.connector

class Update:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Ajay@2002',
            database='Bank'
        )

    def update_employee_record(self, emp_id, emp_name, emp_salary):
        cursor = self.connection.cursor()
        update_query = "UPDATE Employee SET Emp_name=%s, Emp_salary=%s WHERE Emp_id=%s"
        record_data = (emp_name, emp_salary, emp_id)
        cursor.execute(update_query, record_data)
        self.connection.commit()
        print("Record is Updated...")

    def close_connection(self):
        self.connection.close()

def main():
    db_manager = Update()

    emp_id = int(input("Enter Employee Id: "))
    emp_name = input("Enter Employee Name: ")
    emp_salary = int(input("Enter Employee Salary: "))

    db_manager.update_employee_record(emp_id, emp_name, emp_salary)

    db_manager.close_connection()

if __name__ == "__main__":
    main()
