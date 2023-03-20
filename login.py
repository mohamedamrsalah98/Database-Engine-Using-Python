import re
import psycopg2


dbuser = 'postgres'
dbpassword = '12345'
dbname = 'python9'


def validatelogin():
    print("---------------- login ---------------- ")

    email = input("please enter your email : ")
    while not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Not Valid email")
        email = input("please enter your email : ")
    else:
        connection = psycopg2.connect(
            user=dbuser, password=dbpassword, host='127.0.0.1', port='5432', database=dbname)
        dbcursor = connection.cursor()
        selectemail = f"select useremail from usersdata;"
        dbcursor.execute(selectemail)
        connection.commit()
        emails = dbcursor.fetchall()
        for em in emails:
            if em[0] == email:
                password = input("please enter your Password : ")
                selectpassword = "select userpassword from usersdata where useremail = '" + \
                    em[0] + "'"
                dbcursor.execute(selectpassword)
                connection.commit()
                passwords = dbcursor.fetchall()

                while not passwords[0][0] == password:
                    print("not valid password")
                    password = input("please enter your Password : ")
                else:
                    ######################### MenuProject #########################
                    def project():
                        print("-------------- MenuProject --------------")

                        def MenuProject():
                            print("(1) create project")
                            print("(2) view all project")
                            print("(3) delete your project")
                            print("(4) update your project")
                            print("(5) Exit")

                        MenuProject()
                        option = input("enter your option: ")
                        while option != "1" and option != "2" and option != "3" and option != "4" and option != "5":
                            option = input(
                                "please choose 1 or 2 or 3 or 4 or 5 only")

                    ############################## create project #########################
                        else:
                            if option == "1":
                                title = input("enter your title: ")
                                while not title.isalpha():
                                    print("not valid (empty)")
                                    title = input("enter your title: ")
                                else:
                                    Details = input("enter your Details: ")
                                    while Details == "":
                                        print("not valid (empty)")
                                        Details = input(
                                            "enter your Details: ")
                                    else:
                                        Target = input(
                                            "enter your Target: ")
                                        while not Target.isnumeric():
                                            print("please enter numbers")
                                            Target = input(
                                                "enter your Target : ")
                                        else:
                                            dbcursor = connection.cursor()
                                            selectId = f"select id from usersdata where useremail = '{email}';"
                                            dbcursor.execute(selectId)
                                            id = dbcursor.fetchall()
                                            global ID
                                            ID = id[0][0]
                                            connection.commit()
                                            insetTable = f"insert into projects (userid,title,Details,Target) values ('{ID}','{title}','{Details}','{Target}')"
                                            dbcursor.execute(insetTable)
                                            connection.commit()
                                            project()
                        ######################### view all project #########################
                            elif option == "2":
                                dbcursor = connection.cursor()
                                selectId = f"select id from usersdata where useremail = '{email}';"
                                dbcursor.execute(selectId)
                                id = dbcursor.fetchall()
                                ID = id[0][0]
                                viewProject = f"select * from projects where userid ='{ID}';"
                                dbcursor.execute(viewProject)
                                connection.commit()
                                viewAllProject = dbcursor.fetchall()
                                print(viewAllProject)
                                project()

                        ######################### Deleted project #########################

                            elif option == "3":
                                record = input(
                                    "enter name of project you will delete it : ")
                                dbcursor = connection.cursor()
                                selectId = f"select id from usersdata where useremail = '{email}';"
                                dbcursor.execute(selectId)
                                id = dbcursor.fetchall()
                                ID = id[0][0]
                                delete_record = f"delete from projects where title = '{record}' and userid ='{ID}'"
                                dbcursor.execute(delete_record)
                                connection.commit()
                                project()

                        ######################### update project #########################
                            elif option == "4":
                                updateProject = input(
                                    "please enter the project title you want to update")
                                while updateProject == "":
                                    print("not valid projectName (empty)")
                                    updateProject = input(
                                        "please enter the project title you want to update")
                                else:
                                    dbcursor = connection.cursor()
                                    selectId = f"select id from usersdata where useremail = '{email}';"
                                    dbcursor.execute(selectId)
                                    id = dbcursor.fetchall()
                                    ID = id[0][0]
                                    update = f"select title from projects where userid='{ID}'"
                                    dbcursor.execute(update)
                                    connection.commit()
                                    projects = dbcursor.fetchall()
                                    for proj in projects:
                                        if proj[0] == updateProject:
                                            print("(1) update title")
                                            print("(2) update details")
                                            print("(3) update target")
                                            option = input("eter option : ")
                                            while option != "1" and option != "2" and option != "3":
                                                option = input(
                                                    "please choose 1 or 2 or 3 only")
                                            else:
                                                if option == "1":
                                                    newTitle = input(
                                                        "enter the new project name")
                                                    while newTitle == "":
                                                        print(
                                                            "Project name cannot be empty")
                                                        newTitle = input(
                                                            "Please enter a valid project name")
                                                    else:
                                                        updateTitle = f"update projects set title='{newTitle}' where userid='{ID}' and title='{updateProject}'"
                                                        dbcursor.execute(
                                                            updateTitle)
                                                        connection.commit()
                                                        print(
                                                            "newTitle updated susuccessfully")
                                                        project()
                                                elif option == "2":
                                                    newDetails = input(
                                                        "enter the new details")
                                                    while newDetails == "":
                                                        print(
                                                            "Project description cannot be empty")
                                                        newDetails = input(
                                                            "enter the new details")
                                                    else:
                                                        updateDetails = f"update projects set details='{newDetails}' where userid='{ID}' and title='{updateProject}'"
                                                        dbcursor.execute(
                                                            updateDetails)
                                                        connection.commit()
                                                        print(
                                                            "project details updated successfully")
                                                        project()
                                                else:
                                                    newTarget = input(
                                                        "enter the new target")
                                                    while not newTarget.isnumeric():
                                                        print(
                                                            "not valid target")
                                                        newTarget = input(
                                                            "enter the new Target")
                                                    else:
                                                        updateTarget = f"update projects set Target='{newTarget}' where userid='{ID}' and title='{updateProject}'"
                                                        dbcursor.execute(
                                                            updateTarget)
                                                        connection.commit()

                                                        print(
                                                            "project Target updated successfully")

                                                        project()
                            else:
                                dbcursor.close()
                                connection.close()
                                exit()

                    project()
                    break
        else:
            print("not valid email")
            validatelogin()


validatelogin()
