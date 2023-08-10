import mysql.connector

# Replace 'root' and 'localhost' with your MySQL root username and password
username = 'root'
password = 'root'
database_name = 'se4ida'

# Connect to the MySQL server
try:
    connection = mysql.connector.connect(
        host='localhost',
        user=username,
        password=password
    )
    cursor = connection.cursor()

    # Create the database 'se4idata'
    cursor.execute(f"CREATE DATABASE {database_name}")


    # Grant all privileges to the user 'root'@'localhost' for the 'se4idata' database
    cursor.execute(f"GRANT ALL PRIVILEGES ON {database_name}.* TO '{username}'@'localhost'")

    # Flush the privileges to apply the changes
    cursor.execute("FLUSH PRIVILEGES")

    print(f"Database '{database_name}' created. User '{username}' with all privileges granted.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the connection and cursor
    if connection.is_connected():
        cursor.close()
        connection.close()







from sqlalchemy import create_engine

# Replace 'username', 'password', 'host', 'port', and 'se4idata' with your MySQL server details
# The default port for MySQL is 3306
connection_string = 'mysql+mysqlconnector://root:root@localhost:3306/se4idatatest'
engine = create_engine(connection_string)

# Test the connection
try:
    engine.connect()
    print("Connection to 'se4idata' database successful!")
except Exception as e:
    print(f"Connection failed: {e}")