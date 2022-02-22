#Registration and Login system with Python, file handling

while True:
    import re
    import string
    import json

    # if json file does not exist the try statement will generate a json file at the start itself
    try:
        with open("sample_file.json", "x+") as file:
            file.write('{"email":"password"}')

    # if json file already exists the except statement will run through the program
    except:
        while True:
            base = int(input("To register press 1,"
                             "To login press 2:\n"))
            # Registration
            if base == 1:
                # email check
                while True:
                    email = input("Enter a valid email:")
                    compare = []

                    with open("sample_file.json", "r+") as ofile:
                        check = json.load(ofile)
                    if email in check:
                        print("email already exist")
                        continue

                    if "@" in email and "." in email:
                        compare.append(1)
                        test1 = re.findall(r"\B@", email)
                        if bool(test1) == True:
                            print("the user name is invalid,"
                                  "please enter a valid user name")
                            continue
                        else:
                            compare.append(1)

                        test2 = email.split("@")
                        test2[1] = "@" + test2[1]

                        if test2[1].index(".") - test2[1].index("@") == 1:
                            print(f"please provide a valid email provider's name (@?.)")
                            continue
                        else:
                            compare.append(1)

                        if (test2[0][0]).isnumeric() or (test2[0][0]) in string.punctuation:
                            print("user name should not start with special characters and numbers")
                            continue
                        else:
                            compare.append(1)
                    else:
                        print("email should contain @ and .")
                        continue

                    if sum(compare) == 4:
                        break

                # Password check
                while True:
                    password = input("Enter a valid password:")
                    compare_p = []

                    # test1:
                    if len(password) <= 5 or len(password) >= 16:
                        print("The length of password should be between 5-16 characters")
                        continue
                    else:
                        compare_p.append(1)

                    # test2:
                    t2 = re.findall("\W", password)
                    if bool(t2) == False:
                        print("Password must have minimum one special character")
                        continue
                    else:
                        compare_p.append(1)

                    # test3:
                    t3 = re.findall("\d", password)
                    if bool(t3) == False:
                        print("Password must have minimum one digit")
                        continue
                    else:
                        compare_p.append(1)

                    # test4:
                    t4 = re.findall("[A-Z]", password)
                    if bool(t4) == False:
                        print("Password must have minimum one uppercase character")
                        continue
                    else:
                        compare_p.append(1)

                    # test5:
                    t4 = re.findall("[a-z]", password)
                    if bool(t4) == False:
                        print("Password must have minimum one lowercase character")
                        continue
                    else:
                        compare_p.append(1)

                    if sum(compare_p) == 5:
                        break

                with open("sample_file.json", "r+") as file:
                    data = json.load(file)
                    data.update({f"{email}": f"{password}"})
                    file.seek(0)
                    json.dump(data, file)
                    continue

            # login
            elif base == 2:
                with open("sample_file.json", "r+") as ofile:
                    check = json.load(ofile)
                    # print(check)

                check_email = input("Enter a valid email:")
                check_password = input("Enter password:")
                if check_email not in check:
                    print("email id does not exist")
                    continue

                if check[f"{check_email}"] == f"{check_password}":
                    print("!!!you are logged in!!!")
                    continue

                else:
                    print(f" You entered a wrong password")
                    error = int(input("To exit press 1,"
                                      "to retrive password press 2:\n"))
                    if error == 2:
                        print("After verification of otp")
                        print("your password is:", check[f"{check_email}"])
                        continue

                    else:
                        continue

                break








