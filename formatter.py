import os
from time import sleep
try:
    from datetime import datetime
except:
    os.system("pip install datetime")
    from datetime import datetime


now = datetime.now()
dt_string = now.strftime("%d-%m-%Y")

def create(name):
    if not os.path.exists(name):
        os.mkdir(name)
        
def formatter_one():
    tokens = open("tokens.txt", "r").read().splitlines()
    for tokenss in tokens:
        token = tokenss.split(":")[2]
        create("Log")
        create(os.path.join("Log/", dt_string))
        with open(f"Log/{dt_string}/tokens.txt","a+") as file:
            file.write(f"{token}\n")
           
def formatter_two():
    tokens = open("tokens.txt", "r").read().splitlines()
    for tokenss in tokens:
        token = tokenss.split(":")[2]
        passw = tokenss.split(":")[1]
        create("Log")
        create(os.path.join("Log/", dt_string))
        with open(f"Log/{dt_string}/tokens.txt","a+") as file:
            file.write(f"{token}:{passw}\n")
            
def formatter_three():
    tokens = open("tokens.txt", "r").read().splitlines()
    for tokenss in tokens:
        token = tokenss.split(":")[2]
        passw = tokenss.split(":")[1]
        email = tokenss.split(":")[0]
        create("Log")
        create(os.path.join("Log/", dt_string))
        with open(f"Log/{dt_string}/tokens.txt","a+") as file:
            file.write(f"{token}:{email}{passw}\n")
def menu():
    os.system("cls")
    print("""
    [1] Email:pass:token to token
    [2] Email:pass:token to token:pass
    [3] Email:pass:token to token:email:pass""")
    print()
    choice = input("Whats your choice: ")
    if choice == "1":
        formatter_one() 
    elif choice == "2":
        formatter_two() 
    elif choice == "3":
        formatter_three() 
    else:
        print("Wrong choice!")
        sleep(1)
        menu()

    print("Succesfuly completed!")
    sleep(1)
    exit()
menu()