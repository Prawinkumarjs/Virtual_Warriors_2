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
    print("---------------------------------------------------------------------------------------------------------------------")
    for employee in result:
        id, name, department, salary, city, email = employee
        print(f"{id}\t{name}\t\t{department}\t\t{salary}\t{city}\t{email}")

    print("\n====================================================================================================================")
        
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
    print("---------------------------------------------------------------------------------------------------------------------")
    # for employee in result:
    #     id, name, department, salary, city, email = employee
    # print(f"{id}\t{name}\t\t{department}\t\t{salary}\t{city}\t{email}")
    if result:
        id, name, department, salary, city, email = result
        print(f"{id}\t{name}\t\t{department}\t\t{salary}\t{city}\t{email}")
    else:
        print("Employee not found.")

    print("\n====================================================================================================================")
        
    currentcurrsor.close()
    connection.close()

displayone()