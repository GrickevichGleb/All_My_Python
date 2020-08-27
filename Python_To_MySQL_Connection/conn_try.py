import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name
            )
        print("Connection to my DB successful")
    except Error as e:
        print(f'Error \'{e}\' occured')

    return connection


con_d = {'host_name': '127.0.0.1',
         'user_name': 'python_proglib',
         'user_password': 'pythonpasswd4567',
         'db_name': 'python_test'}

connection = create_connection(**con_d)


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f'Error \'{e}\' occurred')


create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT,
    name TEXT NOT NULL,
    age INT,
    gender TEXT,
    nationality TEXT,
    PRIMARY KEY (id)
)
"""

execute_query(connection, create_users_table)
