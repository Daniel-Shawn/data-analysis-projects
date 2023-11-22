import eel
from mysql.connector import *
from database import *

eel.init('web')


def loginUser(name, passw_param):
    try:
        create_db_connection('localhost', 'root', 'marvelcop', 'mydatabase.sql')
        cursor = mysql.connector.connect().cursor()
        cursor.execute(f"SELECT * FROM users WHERE username = {name}")

        get_pass = cursor.fetchone()
        if passw_param == get_pass[0]:
            print("Success :)")
            return 'success'
        else:
            print("Failed")
            mysql.connector.connect().close()
            return 'failed'
    except Exception as Err:
        print(Err)
        return 'failed'


@eel.expose
def btnLogin(name, passw_param):
    msg = loginUser(name, passw_param)
    eel.login_return(str(msg))


#create_db_connection(host_name, user_name, user_password, db_name)
if __name__ == 'main.py':
    create_db_connection('localhost', 'root', 'marvelcop', 'mydatabase.sql')

eel.start('/pages/index.html', size=(300, 400))
