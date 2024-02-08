import mysql.connector

Connection=mysql.connector.connect (
    host='localhost',
    username='root',
    password='Tanaya@1312'
)
Cursor=Connection.cursor()

database_name = input("Enter Database name : ")

def create_database(Cursor, database_name):
    try:
        query = f"CREATE DATABASE {database_name}"
        Cursor.execute(query)
        print(f"Database '{database_name}' created successfully.")

    except mysql.connector.Error as err:
        if "already exists" in str(err):
            print(f"Database '{database_name}' already exists.")
        else:
            print(f"Error: {err}")

create_database(Cursor, database_name)

Connection.commit()
Connection.close()

