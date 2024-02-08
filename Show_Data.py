import mysql.connector

class Show_Details:
    def Fetch_Department_Records(self):
        Connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Tanaya@1312',
            database='Bank'
        )
        Cursor = Connection.cursor()
        
        select_query = "SELECT * FROM Department"
        Cursor.execute(select_query)
        result = Cursor.fetchall()
        for record in result:
            print(record)
        Cursor.close()
        Connection.close()

def main():
    Obj = Show_Details()
    Obj.Fetch_Department_Records()

if __name__ == "__main__":
    main()