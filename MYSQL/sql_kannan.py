import mysql.connector
import faker
fake=faker.Faker()
connection = mysql.connector.connect(host='localhost', user='root', password='root', database='pythondb')
curser = connection.cursor()
curser.execute("SELECT * FROM employee")
result=curser.fetchall()
# for i in range(2):
    # id=fake.random_number(digits=2)
    # name=fake.name()
    # salary=fake.random_number(digits=5)
    # curser.execute("INSERT INTO emp1 (emp_id, emp_name, salary) VALUES (%s, %s, %s)", (id, name, salary))
    # id=int(input("Enter the emp_id :"))
    # curser.execute("DELETE FROM emp1 WHERE emp_id = %s", (id,))
    # curser.execute("UPDATE emp1 SET salary = %s WHERE emp_id = %s", (22222, id))
    # connection.commit()
print(result)
 