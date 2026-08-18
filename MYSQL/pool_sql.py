from mysql.connector import pooling
poolconnections = pooling.MySQLConnectionPool(
        pool_name="mypool",
        pool_size = 5, 
        host='localhost', 
        user='root', 
        password='root', 
        database='pythondb')

def displayone():
    ids = int(input("Enter ID: "))
    connection1 = poolconnections.get_connection()
    cursor1 = connection1.cursor()
    cursor1.execute("select * from pool where id = %s ",(ids,))
    print(cursor1.fetchone())
    cursor1.close()
    connection1.close()

def displayall():
    connection2 = poolconnections.get_connection()
    cursor2 = connection2.cursor()
    cursor2.execute("select * from pool ")
    print(cursor2.fetchall())
    cursor2.close()
    connection2.close()

def insert():
    name , salary = input("Enter Name : "), float(input("Enter Salary: "))
    id = int(input("Enter ID: "))
    connection3 = poolconnections.get_connection()
    cursor3 = connection3.cursor()
    cursor3.execute("insert into pool(id,name, salary) values(%s,%s,%s)",(id,name, salary))
    connection3.commit()
    cursor3.close()
    connection3.close()
def update():
    ids = int(input("Enter ID: "))

    connection4 = poolconnections.get_connection()
    cursor4 = connection4.cursor()

    cursor4.execute(
        "SELECT * FROM pool WHERE id = %s",
        (ids,)
    )

    result = cursor4.fetchone()

    if result:
        name = input("Enter Name: ")
        salary = float(input("Enter Salary: "))

        cursor4.execute(
            "UPDATE pool SET name = %s, salary = %s WHERE id = %s",
            (name, salary, ids)
        )

        connection4.commit()

        print("Employee Updated Successfully")

    else:
        print("Employee Not Found")

    cursor4.close()
    connection4.close()

def delete():
    connection5 = poolconnections.get_connection()
    currentcursor = connection5.cursor()
    empid = int(input('Enter Employee ID: '))
    currentcursor.execute("SELECT * FROM pool WHERE id=%s",(empid,))
    result = currentcursor.fetchone()  
    if result:
        currentcursor.execute("DELETE FROM pool WHERE id=%s",(empid,))
        connection5.commit()
        print("Employee Deleted Successfully")
    else:
        print("Employee Not Found")
    currentcursor.close()
    connection5.close()

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
            insert()
        elif choice == 2:
            print("Display Operation")
            displayall()
        elif choice == 3:
            print("Display Specific")
            displayone()
        elif choice == 4:
            print("Update Operation")
            update()
        elif choice == 5:
            print('Delete Operation')
            delete()
        elif choice == 6:
            print("Thank you for using Employee Management System.")
            break
        else:
            print("Invalid Choice")



menu()
