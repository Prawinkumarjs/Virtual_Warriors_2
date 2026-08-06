from mysql.connector import pooling
poolconnections = pooling.MySQLConnectionPool(
        pool_name="mypool",
        pool_size = 2, 
        host='localhost', 
        user='root', 
        password='root', 
        database='pythondb')
connection1 = poolconnections.get_connection()
# table pool for this