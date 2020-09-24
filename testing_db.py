import mysql.connector
import datetime
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
def showcategories():
    prompt=True
    while(prompt):
        print("List of categories available: ")
        print("1. T-Shirts")
        option=input("Choose option: ")
        option=option.strip()
        if(option==str(1)):
            return("tshirts")
            prompt=False
        else:
            print("option invalid.")

def insert(con):
    option=showcategories()
    date=str(datetime.date.today())
    print(date)
    cursor = con.cursor()
    print(cursor)
    print("Enter values as prompted.")
    pid=input("Enter product id: ")
    description=input("Enter product description: ")
    price=input("Enter product price: ")
    sold="No"
    sql=f"INSERT INTO tshirts VALUES('{pid}', '{description}', '{date}', '{price}', '{sold}');"
    print(f"SQL to be executed: {sql}")
    cursor.execute(sql)
    con.commit()
    cursor.close()
    con.close()

# def update(con):
# def delete(con):


    

def main():
    # prompt1_1()
    con=connnect2db()
    print(f"connection object retreived: {con}")
    insert(con)

    con.close()
    

if __name__ == '__main__':
  main()