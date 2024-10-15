import mysql.connector
def create_connection():
    try:
        connection = mysql.connector.connect(
            user = "root", 
            password = "root", 
            host = "localhost", 
            database = "mysql_python"
            )
        return connection

    except Exception:
        print("Some problem occuerd")
        return None