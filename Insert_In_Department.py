import mysql.connector

class Insertion:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Tanaya@1312',
            database='Bank'
        )
        self.cursor = self.connection.cursor()

    def insert_department_record(self, dept_id, dept_name):
        insert_query = "INSERT INTO Department (Dept_id, Dept_Name) VALUES (%s, %s)"
        record_data = (dept_id, dept_name)
        self.cursor.execute(insert_query, record_data)
        self.connection.commit()
        print("New Data is Inserted.")

    def close_connection(self):
        self.connection.close()

def main():
    obj = Insertion()

    dept_id = int(input("Enter Department Id : "))
    dept_name = input("Enter Department Name : ")

    obj.insert_department_record(dept_id, dept_name)
    obj.close_connection()

if __name__ == "__main__":
    main()
