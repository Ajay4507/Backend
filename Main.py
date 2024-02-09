import mysql.connector

class Bank_Database:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Ajay@2002',
            database='Bank'
        )
        self.cur = self.mydb.cursor()

    def display_menu(self):
        print()
        print("1. Create Table")
        print("2. Insert Data")
        print("3. Update Data")
        print("4. Display Data")

    def create_table(self):
        print()
        print("You Selected Create Table..")
        from CreateTable import main
        main()

    def insert_data(self):
        print()
        print("You Selected Insert Data..")
        from Insert_Employee import main
        main()

    def update_data(self):
        print()
        print("You Selected Update Data..")
        from Update_Employee import main
        main()

    def display_data(self):
        print()
        print("You Selected Display Data")
        from Display_Employee import main
        main()
        
    def run(self):
        while True:
            self.display_menu()
            choice = int(input("Enter Your Choice (0 to exit): "))
            
            if choice == 0:
                break
            elif choice == 1:
                self.create_table()
            elif choice == 2:
                self.insert_data()
            elif choice == 3:
                self.update_data()
            elif choice == 4:
                self.display_data()
            else:
                print("Invalid Choice...")
        
        print("Thank You...")

if __name__ == "__main__":
    bank_system = Bank_Database()
    bank_system.run()

