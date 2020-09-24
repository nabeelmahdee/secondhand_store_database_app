import mysql.connector
def connnect2db():
    config = {
        'user': 'root',
        'password': 'admin',
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

def insert(con):
    
def update(con):
def delete(con):


    

def main():
    # prompt1_1()
    con=connnect2db()
    print(f"con object retreived: {con}")

    con.close()
    

if __name__ == '__main__':
  main()