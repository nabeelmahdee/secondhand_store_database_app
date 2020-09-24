#!/usr/bin/python -tt
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

#the prompt1 function will return the selection made and it is the first thing that will run
#upon opening the program
def prompt1():
    prompt = True
    while(prompt):
        print("Make a selection: ")
        print
        print("1. Add/Update Entry")
        print("1. Check Inventory")
        print("2. Sell Items")
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


#the main fucntion
def main():
    selection = prompt1()
    selection=prompt1_1(selection)
    # connnect2db()

if __name__ == '__main__':
  main()
