# Nested ifs

username = input("Input your username:\n")
password = input("And now password:\n")

if username == "Neo":
    if password == "password":
        print("Welcome to the Matrix, {}".format(username))
    else:
        print("Wrong password:")
else:
    print("Wrong username!")
        
