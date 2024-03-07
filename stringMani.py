# firstName = input("What is your first name ")
# lastName = input("What is your last name ")
# accountBalance = input("what is your account balance ")
# accountNumber = input("what is your account number ")
# print(firstName.capitalize())
# print(firstName.upper())
# print(firstName.lower())

# print(f"Hi {firstName.capitalize()} {lastName.capitalize()}.\nYour Account balance is ${accountBalance}\nYour Account Number is {accountNumber}")
# print(f'''Hi {firstName.capitalize()} {lastName.capitalize()}.
# Your Account balance is ${accountBalance}
# Your Account Number is {accountNumber}''')

# Assignment ask student about their scores in science, math and english exam
# Ask for their name, print admission number and find the mean score and write your average score is

# firstName,lastName = input("What is your first name "),input("What is your last name ")
# math = int(input(f'Dear {firstName} {lastName} enter your score in maths exam '))
# science = int(input(f'Dear {firstName} {lastName} enter your score in science exam '))
# english = int(input(f'Dear {firstName} {lastName} enter your score in english exam '))
# add = math + science + english
# mean = add/3
# print(f'''Dear {firstName.capitalize()} {lastName.capitalize()}
# Congratulation you have been offered admission into our University 
# With an average score of {mean}.''') 

product1, price1 = input("What did customer buy "),int(input(f"Enter the amount paid for  "))
product2, price2 = input("What did customer buy "),int(input(f"Enter the amount paid for  "))
product3, price3 = input("What did customer buy "),int(input(f"Enter the amount paid for  "))
print(f'''
Product Price
{product1}  ${price1}
{product2}  ${price2}
{product3}  ${price3}
''')
