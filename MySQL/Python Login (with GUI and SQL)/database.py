import mysql.connector


# ///A function to connect to our MySQL Server
def create_server_connection(host_name, db_user_name, db_user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=db_user_name,
            passwd=db_user_password
        )
        print("MySQL Database connection successful")
    except Exception as err:
        print(f"Error: '{err}'")
    return connection


# /////////////////Connecting to the Database
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print(f"MySQL connection to database: {db_name} is successful")
    except Exception as err:
        print(f"Error: '{err}'")
    return connection


# /////////////////// Creating a Query Execution Function
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Exception as err:
        print(f"Error: '{err}'")
