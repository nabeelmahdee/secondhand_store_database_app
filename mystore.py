#!/usr/bin/python -tt
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

#the prompt1 function will return the selection made and it is the first thing that will run
#upon opening the program
def prompt1():
    prompt = True
    while(prompt):
        print("Make a selection: ")
        print
        print("1. Add/Update Entry")
        print("2. Check Inventory")
        print("3. Sell Items")
        selection = input(": ")
        if(selection==str(1)):
            print("You selected Add/Update Entry")
            prompt=False
            return(1)
        elif(selection==str(2)):
            print("You selected Check Inventory")
            prompt=False
            return(2)
        elif(selection==str(3)):
            print("You selected Sell Items")
            prompt=False
            return(3)
        else:
            print("Invalid Selection. Enter correct number.")

def showcategories():
    prompt=True
    print("List of categories available: ")
    print("1. T-Shirts")
    print("2. Electronics")
    option=input("Choose option: ")
    option=option.strip()
    if(option==str(1)):
        return("tshirts")
        prompt=False
    elif(option==str(2)):
        return("electronics")
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
    sql=f"INSERT INTO {option} VALUES('{pid}', '{description}', '{date}', '{price}', '{sold}');"
    print(f"SQL to be executed: {sql}")
    print("Done.")
    cursor.execute(sql)
    con.commit()
    cursor.close()
    con.close()

def finditem(con):
    cursor=con.cursor()
    item_id=input("Enter Item Id: ")
    item_id=item_id.strip()
    query=f"SHOW TABLES;"
    print(f"SQL to be executed: {query}")
    query=str(query)
    cursor.execute(query)
    print(cursor)
    print("query carried out successfully")

    tables=[]
    for table in cursor:
        tables.append(table[0])
        print(tables) # printed for debugging purposes

    for table in tables:
       query=f"SELECT * FROM {table} WHERE item_id='{item_id}';" 
       print(f"SQL to be executed: {query}")
       query=str(query)
       cursor.execute(query)
       print(cursor)
       print("query carried out successfully")
       for(item_id, description, date, price, sold) in cursor:
        print("Item Id: {}\nDescription: {}\nDate of entry: {}\nPrice: {}\nSold: {}".format(item_id, description, date, price, sold)) 

# Prompt appearing after selectig the first option
def prompt1_1(selection):
    if(selection==1):
        prompt=True
        while(prompt):
            print("What would you like to do?")
            print
            print("1. Make an entry")
            print
            print("2. Update existing entry")
            print
            print("3. Delete existing entry")
            selection=input(": ")

            if(selection==str(1)):
                print("you have chosen to make an entry")
                prompt=False
                return(1)
            elif(selection==str(2)):
                print("you have chosen to update an existing entry")
                prompt=False
                return(2)
            elif(selection==str(3)):
                print("you have chosen to delete an existing entry")
                prompt=False
                return(3)
            else:
                print("Invalid selection")
    if(selection==2):
        return 2

def run_prompt_1_1(selection):
    if(selection==1):
        con=connnect2db()
        insert(con)
    elif(selection==2):
        con=connnect2db()
        finditem(con)
    elif(selection==3):
        print("To be added in the future.")
#the main function
def main():
    selection = prompt1()
    selection=prompt1_1(selection)
    run_prompt_1_1(selection)

if __name__ == '__main__':
  main()
