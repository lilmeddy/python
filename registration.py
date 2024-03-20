
user =[]

for users in range(3):
      firstName,lastName,password = input("Enter your first name\n"),input("Enter your last name\n"),input("Enter your password\n")
      while len(password) < 10 :
           print("Password must be greater than 10 characters")
           password = input("Enter your password\n")
           user.append([firstName,lastName,password])
print(user)


