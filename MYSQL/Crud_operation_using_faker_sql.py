from mysql.connector import*
import faker
import random

def connect_database():
    connector = connect(
        host='localhost',
        user='root',
        password='root',
        database='pythondb'
    )
    return connector

fake = faker()
