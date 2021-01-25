import json
import getpass

# Clean up look of json file

def write(acc_type, acc_cred, acc_pass):

    data = {
        acc_type: {
            "Login": acc_cred,
            "Password": acc_pass
        }
    }

    with open("passwords.json", "a+") as write_file:

        json.dump(data, write_file)

print("")
print("Generic title screen")
print("")

acc_type = str(input("Type please: "))
acc_cred = str(input("User/email please: "))
acc_pass = getpass.getpass()

write(acc_type, acc_cred, acc_pass)
