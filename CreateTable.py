import mysql.connector

def connect_to_database(host, username, password, database):
    return mysql.connector.connect(
        host=host,
        user=username,
        password=password,
        database=database
    )

def create_table(connection, table_name, columns):
    cursor = connection.cursor()
    try:
        query = f"CREATE TABLE {table_name} ({columns})"
        cursor.execute(query)
        print(f"Table '{table_name}' created successfully.")

    except mysql.connector.Error as err:
        if "already exists" in str(err):
            print(f"Table '{table_name}' already exists.")
        else:
            print(f"Error: {err}")

def main():
    host = 'localhost'
    username = 'root'
    password = 'Ajay@2002'
    database = 'Bank'

    connection = connect_to_database(host, username, password, database)

    table_name = input("Enter table name: ")
    columns = input("Enter column details: ")

    create_table(connection, table_name, columns)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    main()
