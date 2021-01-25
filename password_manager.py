# Written by Linus Gorecki
# Version 0.0.1

import json 
import getpass 
import sys

def write(acc_type, acc_cred, acc_pass): 

    data = {
        acc_type: {
            "Login": acc_cred,
            "Password": acc_pass
        }
    }

    with open("passwords.json", "a+") as fobj:

        json.dump(data, fobj)
        fobj.write("\n")

def read():

    fobj = open("passwords.json", "r")

    print("")
    print(fobj.read())

def remove():

    print("")
    search_type = str(input("Please enter the type of account you would like to remove: "))
    print("ATTENTION! Every account of the specified type will be removed from the password manager!")
    cont = str(input("Would you like to continue? Y or N: "))
    print("")

    if cont == "Y":

        search = '{"%s' % (search_type)

        with open("passwords.json", "r") as fobj: 
            lines = fobj.readlines()

        with open("passwords.json", "w") as fobj:
            for line in lines: 
                if not line.startswith(search):
                    fobj.write(line)

    else: 

        sys.exit(0)

print("")
print("  ___                              _                                     ")
print(" | _ \__ _ _______ __ _____ _ _ __| |  _ __  __ _ _ _  __ _ __ _ ___ _ _ ")
print(" |  _/ _` (_-<_-< V  V / _ \ '_/ _` | | '  \/ _` | ' \/ _` / _` / -_) '_|")
print(" |_| \__,_/__/__/\_/\_/\___/_| \__,_| |_|_|_\__,_|_||_\__,_\__, \___|_|  ")
print("                                                           |___/         ")
print("")
print("(1)  Add a new account")
print("(2)  Look at existing accounts")
print("(3)  Remove an account")
print("(99) Exit")
print("")

action = int(input("What would you like to do: "))

if action == 99:

    print("")
    sys.exit(0)

while action != 99: 

    if action == 1: 

        print("")

        acc_type = str(input("Please enter the account type: "))
        acc_cred = str(input("Please enter your username or email-address: "))
        acc_pass = getpass.getpass("Please enter your password: ")
        print("")

        write(acc_type, acc_cred, acc_pass)

        action = int(input("What would you like to do: "))

    elif action == 2: 

        read()

        action = int(input("What would you like to do: "))

    elif action == 3: 

        remove()

        action = int(input("What would you like to do: "))