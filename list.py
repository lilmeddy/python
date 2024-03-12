# assignment
# create an origin list of your classmates
# ask for the names of 5 student add each of them to a list
# merge both list together 
# ask for a name the user want to search for 
# print the index of the name


# the original list of my matess
classNames = ["Osamede", "Obafemi", "Damola","Duro","Ibrahim"]
# asking for names 
firstName, secondName,thirdName,fourthName,fithName = input("Enter your name: "),input("Enter your name: "),input("Enter your name: "),input("Enter your name: "),input("Enter your name: ")
# merging them together 
classNames.extend([firstName, secondName, thirdName,fourthName,fithName])
print(classNames)
#  asking search for a name 
searchName = input("Search for a name: ")
# searching the name 
searchClass = classNames.index(searchName)
# printing the index 
print(searchClass)