from mysql.connector import *

# def connect_database():
#     connector = connect(host='localhost', user='root', password='root', database='pythondb')
#     currentcursor = connector.cursor()
#     return connector, currentcursor

def connect_database():
    connector = connect(
        host='localhost',
        user='root',
        password='root',
        database='pythondb'
    )
    return connector

def insert_employee():
    # connect database
    connector = connect_database()
    # userinput
    id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))
    # sql query
    currentcursor = connector.cursor()
    currentcursor.execute("INSERT INTO crud VALUES (%s, %s, %s, %s)",(id, name, department, salary))
    # Commit
    connector.commit()
    # Print success message
    print("Insertion Completed")
    # Close cursor
    currentcursor.close()
    # Close connection
    connector.close()

def display_all():
    # connect database
    connector = connect_database()
    # create cursor
    currentcursor = connector.cursor()
    # sql query
    currentcursor.execute("select * from crud")
    # fetch data
    result = currentcursor.fetchall()
    # print it in row
    print("\n===== Employee Details =====")
    if result:
        for row in result:
            print("-" * 30)
            print("Employee ID :", row[0])
            print("Name        :", row[1])
            print("Department  :", row[2])
            print("Salary      :", row[3])
    else:
        print("No Employee Found")
    # Close cursor
    currentcursor.close()
    # Close connection
    connector.close()

def display_by_id():
    # connect database
    connector = connect_database()
    # create cursor
    currentcursor = connector.cursor()
    # user input
    id = int(input("Enter Employee ID: "))
    # sql query
    currentcursor.execute("select * from crud where id = %s ", (id,))
    # fetch data
    result = currentcursor.fetchone()
    # print it in row
    print("\n===== Employee Details =====")
    if result:
        print("-" * 30)
        print("Employee ID :", result[0])
        print("Name        :", result[1])
        print("Department  :", result[2])
        print("Salary      :", result[3])
        print("-" * 30)
    else:
        print("No Employee Found")
    # Close cursor
    currentcursor.close()
    # Close connection
    connector.close()

def update_employee():
    # connect database
    connector = connect_database()
    # create cursor
    currentcursor = connector.cursor()
    # get empid
    empid = int(input('Enter Employee ID: '))
    # check whether emp is not 
    currentcursor.execute("SELECT * FROM crud WHERE id=%s",(empid,))
    result = currentcursor.fetchone()   

    if result:
        name = input("Enter New Name: ")
        department = input("Enter New Department: ")
        salary = float(input("Enter New Salary: "))
        currentcursor.execute("update crud set name = %s, department = %s,salary=%s WHERE id=%s ",(name, department, salary, empid))
        # Commit
        connector.commit()
        # Print success message
        print("Employee Updated Successfully")

    else:
        print("Employee Not Found")

    # Close cursor
    currentcursor.close()
    # Close connection
    connector.close()


def delete_employee():
    # connect database
    connector = connect_database()
    # create cursor
    currentcursor = connector.cursor()
    # get empid
    empid = int(input('Enter Employee ID: '))
    # check whether emp is not 
    currentcursor.execute("SELECT * FROM crud WHERE id=%s",(empid,))
    result = currentcursor.fetchone()  
    if result:
        # Delete
        currentcursor.execute("DELETE FROM crud WHERE id=%s",(empid,))
        connector.commit()
        print("Employee Deleted Successfully")
    else:
        print("Employee Not Found")

    # Close cursor
    currentcursor.close()
    # Close connection
    connector.close()


def menu():
    while True:
        print("\n1.Insert")
        print("2.Display")
        print("3.Search")
        print("4.Update")
        print("5.Delete")
        print("6.Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Insert Operation")
            insert_employee()
        elif choice == 2:
            print("Display Operation")
            display_all()
        elif choice == 3:
            print("Display Specific")
            display_by_id()
        elif choice == 4:
            print("Update Operation")
            update_employee()
        elif choice == 5:
            print('Delete Operation')
            delete_employee()
        elif choice == 6:
            print("Thank you for using Employee Management System.")
            break
        else:
            print("Invalid Choice")



menu()