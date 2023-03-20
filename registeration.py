
import re
import os


import psycopg2
dbuser = 'postgres'
dbpassword = '12345'
dbname = 'python9'


try:
    connection = psycopg2.connect(
        user=dbuser, password=dbpassword, host='127.0.0.1', port='5432', database=dbname)

except (Exception, psycopg2.Error) as e:
    print(e)


print("---------------- registeration ---------------- ")

############################# FirstName #############################


def validateFirstName():
    FirstName = input("please enter your FirstName : ")
    while not FirstName.isalpha():
        print("Not Valid Name")
        FirstName = input("please enter your FirstName : ")
    else:
        return FirstName


FirstName = validateFirstName()

############################# LastName #############################


def validateLastName():
    LastName = input("please enter your LastName : ")
    while not LastName.isalpha():
        print("Not Valid Name")
        LastName = input("please enter your LastName : ")
    else:
        return LastName


LastName = validateLastName()

############################# Email #############################


def validatingEmail():

    email = input("please enter your email : ")
    while not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Not Valid email")
        email = input("please enter your email : ")

    else:
        return email
        # for x in range(len(users)):
        #     while users[x].split(":")[3] == email:
        #         print(f"{email} is already registered ")
        #         print("enter a new email")
        #         email = input()


email = validatingEmail()

############################# Password #############################


def validatePassword():
    password = input("please enter your Password : ")
    import re
    while len(password) < 8 or not re.search('[0-9]', password) or not re.search('[A-Z]', password):
        print("Not Valid password is at lest 8 letters or has a number in it or has a capital letter in it")
        password = input("please enter your Password : ")
    else:
        return password


password = validatePassword()

############################# ConfirmPassword #############################


def validateConfirmPassword():
    ConfirmPassword = input("please enter your ConfirmPassword : ")
    while not ConfirmPassword == password:
        print("Not Valid ConfirmPassword")
        ConfirmPassword = input("please enter your ConfirmPassword : ")
    else:
        return ConfirmPassword


ConfirmPassword = validateConfirmPassword()

############################# Phone #############################


def validatePhone():
    Phone = input("please enter your Phone : ")
    import re
    while not re.match(r"^01[0-9]{9}$", Phone):
        print("Not Valid Phone")
        Phone = input("please enter your Phone : ")
    else:
        return Phone


Phone = validatePhone()

############################## insert ##################################

dbcursor = connection.cursor()
query_insert = f"insert into usersdata (username, lastname,useremail,userpassword,usermobile) values ('{FirstName}','{LastName}','{email}','{password}',{Phone})"
dbcursor.execute(query_insert)
connection.commit()
dbcursor.close()
connection.close()
os.system("python3 login.py")
