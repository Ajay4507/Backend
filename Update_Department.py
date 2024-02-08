import mysql.connector

class Updation:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Tanaya@1312',
            database='Bank'
        )
        self.cursor = self.connection.cursor()

    def update_department_record(self, dept_id, dept_name):
        update_query = "UPDATE Department SET Dept_Name=%s WHERE Dept_id=%s"
        record_data = (dept_name, dept_id)
        self.cursor.execute(update_query, record_data)
        self.connection.commit()
        print("The Record is Updated Successfully.")

    def close_connection(self):
        self.connection.close()

def main():
    obj = Updation()

    dept_id = int(input("Enter Department Id: "))
    dept_name = input("Enter Department Name: ")

    obj.update_department_record(dept_id, dept_name)

    obj.close_connection()

if __name__ == "__main__":
    main()
