
user =[]

for users in range(5):   
    userName =input("Enter your username\n")
    for i in user:
       while i[0] == userName:
            print("UserName taken")
            userName= input("Enter your user name\n")
    lastName,password = input("Enter your last name\n"),input("Enter your password\n")
    while len(password) < 10 :
        print("Password must be greater than 10 characters")
        password = input("Enter your password\n")

    user.append([userName,lastName,password])
print(user)

# login

