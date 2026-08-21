from mysql.connector import*
from faker import Faker
import random

def connect_database():
    connector = connect(
        host='localhost',
        user='root',
        password='root',
        database='pythondb'
    )
    return connector
def generatefaker():
    fake = Faker()
    # id = 1001
    name = fake.name()
    city = fake.city()
    email = fake.email()
    departments = ["IT","Admin","Finance","Marketing","Sales"]
    department = random.choice(departments)
    salary = random.randint(30000,90000)
    return (name, department, salary, city, email)

def insert():
    connection = connect_database()
    # faker input
    data = generatefaker()
    # sql query
    currentcursor = connection.cursor()
    currentcursor.execute("INSERT INTO fakeremployee"
                        "( name, department, salary, city, email)" \
                        "VALUES ( %s, %s, %s, %s, %s)",data)

    # commit
    connection.commit()
     # Print success message
    print("Insertion Completed")
    # Close cursor
    currentcursor.close()
    # Close connection
    connection.close()

def displayall():

    connection = connect_database()
    currentcurrsor = connection.cursor()
    currentcurrsor.execute("SELECT * FROM fakeremployee")
    result = currentcurrsor.fetchall()
    print("\n============================================Employee Details=======================================================")
    print("ID\tName\t\t\tDepartment\tSalary\t\tCity\t\tEmail")
    print("-------------------------------------------------------------------------------------------------------------------")
    for employee in result:
        id, name, department, salary, city, email = employee
        print(f"{id}\t{name}\t\t{department}\t\t{salary}\t{city}\t{email}")

    print("\n===================================================================================================================")
        
    currentcurrsor.close()
    connection.close()

def displayone():

    connection = connect_database()
    currentcurrsor = connection.cursor()
    id = int(input("Enter Employee ID: "))
    currentcurrsor.execute("SELECT * FROM fakeremployee where id = %s",(id,))
    result = currentcurrsor.fetchone()
    print("\n============================================Employee Details=======================================================")
    print("ID\tName\t\t\tDepartment\tSalary\t\tCity\t\tEmail")
    print("-------------------------------------------------------------------------------------------------------------------")

    if result:
        id, name, department, salary, city, email = result
        print(f"{id}\t{name}\t\t{department}\t\t{salary}\t{city}\t{email}")
    else:
        print("Employee not found.")

    print("\n===================================================================================================================")
        
    currentcurrsor.close()
    connection.close()

def update():

    connection = connect_database()
    currentcursor = connection.cursor()

    updated = False
    emp_id = int(input("Enter Employee ID: "))
    currentcursor.execute("select * from fakeremployee where id = %s",(emp_id,))
    result = currentcursor.fetchone()
    if result:
        print('\nWhat do you want to do?')
        print("1. Name")
        print('2. Department')
        print("3. Salary")
        print("4. City")
        print("5. Email")

        update_choice = int(input("Enter your Choice: "))

        if update_choice == 1:
            name = input("Enter New Name: ")
            query = "UPDATE fakeremployee SET name = %s WHERE id = %s"
            currentcursor.execute(query,(name,emp_id))
            updated = True

        elif update_choice == 2:
            department = input("Enter New Department: ")
            query = "UPDATE fakeremployee SET department = %s WHERE id = %s"
            currentcursor.execute(query,(department,emp_id))
            updated = True

        elif update_choice == 3:
            salary = float(input("Enter New Salary: "))
            query = "UPDATE fakeremployee SET salary = %s WHERE id = %s"
            currentcursor.execute(query,(salary,emp_id))
            updated = True

        elif update_choice == 4:
            city = input("Enter New City: ")
            query = "update fakeremployee set city = %s where id = %s"
            currentcursor.execute(query,(city,emp_id))
            updated = True

        elif update_choice == 5:
            email = input("Enter New Email: ")
            query = "update fakeremployee set email = %s where id = %s"
            currentcursor.execute(query,(email,emp_id))
            updated = True

        else:
            print("Invalid Choice")

        if updated:
            connection.commit()
            print("Employee Updated Successfully")

    else:
        print("Employee Not Found")

    

    currentcursor.close()
    connection.close()




def update_faker():

    connection = connect_database()
    currentcursor = connection.cursor()
    updated = False

    emp_id = int(input("Enter Employee ID: "))

    currentcursor.execute("SELECT * FROM fakeremployee WHERE id = %s",(emp_id,))

    result = currentcursor.fetchone()

    if result:
        fake = Faker()
        print("\nWhat do you want to update?")
        print("1. Name")
        print("2. Department")
        print("3. Salary")
        print("4. City")
        print("5. Email")

        update_choice = int(input("Enter your choice: "))

        if update_choice == 1:
            old_name = result[1] 
            new_name = fake.name()
            print("Old Name:", old_name)
            print("New Faker Name:", new_name)
            query = "UPDATE fakeremployee SET name = %s WHERE id = %s"
            currentcursor.execute(query,(new_name,emp_id))
            updated = True

        elif update_choice == 2:
            old_department = result[2]
            new_departments = ["IT","Admin","Finance","Marketing","Sales"]
            new_department = random.choice(new_departments) 
            print("Old Department: ", old_department)
            print("New Department: ", new_department)   
            query = "UPDATE fakeremployee SET department = %s WHERE id = %s"
            currentcursor.execute(query,(new_department,emp_id))
            updated = True

        elif update_choice == 3:
            old_salary = result[3]
            new_salary = random.randint(30000,90000)
            print("Old Salary: ", old_salary)
            print("New Salary: ", new_salary)
            query = "UPDATE fakeremployee SET salary = %s WHERE id = %s"
            currentcursor.execute(query,(new_salary,emp_id))
            updated = True

        elif update_choice == 4:
            old_city = result[4]
            new_city = fake.city()
            print("Old City: ", old_city)
            print("New City: ", new_city)
            query = "update fakeremployee set city = %s where id = %s"
            currentcursor.execute(query,(new_city,emp_id))
            updated = True

        elif update_choice == 5:
            old_email = result[5]
            new_email = fake.email()
            print("Old Email: ", old_email)
            print("New Email: ", new_email)
            query = "update fakeremployee set email = %s where id = %s"
            currentcursor.execute(query,(new_email,emp_id))
            updated = True

        else:
            print("Invalid Choice")

        if updated:
            connection.commit()
            print("Employee Updated Successfully")



    else:
        print("Employee Not Found")

    currentcursor.close()
    connection.close()


def delete():

    connection = connect_database()
    currentcursor = connection.cursor()
    emp_id = int(input("Enter Employee ID: "))

    currentcursor.execute("SELECT * FROM fakeremployee WHERE id = %s",(emp_id,))

    result = currentcursor.fetchone()

    print(result)
    # for employee in result:
    #     id, name, department, salary, city, email = employee
    #     print(f"{id}\t{name}\t\t{department}\t\t{salary}\t{city}\t{email}")


    currentcursor.close()
    connection.close()


delete()