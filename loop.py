# range function 
# passing 1 parameter i.e (starts from zero ends at the parameter specified without returning the parameter)
for num in range(10):
    print(num)

# passing 2 parameter i.e (starts fron zero and ends the parameter specified without returning the parameter )
for num in range (4,10):
    print(num)

# passing 3 parameter i.e (starts from first paramter end at second without returning the second at a step of the third-1 e.g 2 step will be 1 )
for num in range (4,10,2):
    print(num) 

numbers =[]
for num in range(3):
    numbers.append(input("Enter a number: "))
print(numbers)