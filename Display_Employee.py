import mysql.connector

class Display:
    def fetch_employee_records(self):
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Ajay@2002',
            database='Bank'
        )
        cursor = connection.cursor()
        select_query = "SELECT * FROM Employee"
        cursor.execute(select_query)
        result = cursor.fetchall()
        for record in result:
            print(record)
        cursor.close()
        connection.close()

def main():
    db_manager = Display()
    db_manager.fetch_employee_records()

if __name__ == "__main__":
    main()
