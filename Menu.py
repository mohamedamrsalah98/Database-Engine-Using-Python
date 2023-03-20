import os
print("----------------- Hello in our Database Engine -----------------")


def Menu():
    print("(1) registeration")
    print("(2) login")


Menu()
option = input("enter your option: ")
while option != "1" and option != "2":
    print("please choose 1 or 2 only")
    option = input("enter your option: ")
else:
    if option == "1":
        os.system("clear")
        os.system("python3 registeration.py")
    else:
        os.system("python3 Menu.py")
