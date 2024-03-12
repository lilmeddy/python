# assignment
# create an origin list of your classmates
# ask for the names of 5 student add each of them to a list
# merge both list together 
# ask for a name the user want to search for 
# print the index of the name



classNames = ["Osamede", "Obafemi", "Damola","Duro","Ibrahim"]
firstName, secondName,thirdName,fourthName,fithName = input("Enter your name: "),input("Enter your name: "),input("Enter your name: "),input("Enter your name: "),input("Enter your name: ")
classNames.extend([firstName, secondName, thirdName,fourthName,fithName])
print(classNames)
searchName = input("Search for a name: ")
searchClass = classNames.index(searchName)
print(searchClass)