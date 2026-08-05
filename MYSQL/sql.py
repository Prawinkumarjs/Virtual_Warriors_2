from mysql.connector import*
connector = connect(host='localhost', user='root', password='root', database='pythondb')
currentcursor = connector.cursor()

# insert
currentcursor.execute("insert into employee values(%s,%s,%s,%s)",(103,"Prithika","CSE","20000"))
connector.commit()

# select
currentcursor.execute('select * from employee ')
result = currentcursor.fetchall()
print(result)

# select where
currentcursor.execute("SELECT * FROM employee WHERE id=%s",(101,))
result = currentcursor.fetchall()
print(result)

# update
currentcursor.execute("update employee set salary = %s where id = %s", (35000,101))
print("After Update salary")
currentcursor.execute('select * from employee')
result = currentcursor.fetchall()
print(result)

# delete
currentcursor.execute("delete from employee where id = %s", (103,))
print("After Delete")
currentcursor.execute('select * from employee')
result = currentcursor.fetchall()
print(result)



currentcursor.close()

connector.commit()
connector.close()