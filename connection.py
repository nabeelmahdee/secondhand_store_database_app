import mysql.connector
import datetime
import getpass

def connnect2db():
    username=input("Enter Database Username: ")
    password=getpass.getpass(prompt="Enter Database Password: ")
    config = {
        'user': f'{username}',
        'password': f'{password}',
        'host': '127.0.0.1',
        'database': 'myshstore',
        'raise_on_warnings': True
    }

    con = mysql.connector.connect(**config)

    if(con):
        print("Connected!")
        print(f"connecton object: {con}")
        print("returning con object...")
        return con