import mysql.connector
from Create_Table import main as create_table
from Insert_In_Department import main as insert_data
from Update_Department import main as update_data
from Show_Data import main as display_data

class Bank:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Tanaya@1312',
            database='Bank'
        )
        self.cursor = self.connection.cursor()

    def display_menu(self):
        print("\n1. Create Table")
        print("2. Insert Data")
        print("3. Update Data")
        print("4. Display Data")

    def run(self):
        while True:
            self.display_menu()
            choice = int(input("Enter Your Choice (0 to exit): "))
            
            if choice == 0:
                break
            elif choice == 1:
                create_table()
            elif choice == 2:
                insert_data()
            elif choice == 3:
                update_data()
            elif choice == 4:
                display_data()
            else:
                print("Invalid Choice...")
        
        print("Thank You...")

if __name__ == "__main__":
    obj = Bank()
    obj.run()
