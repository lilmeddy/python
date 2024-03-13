# assignment
# create an origin list of your classmates
# ask for the names of 5 student add each of them to a list
# merge both list together 
# ask for a name the user want to search for 
# print the index of the name


# the original list of my matess
classNames = ["Osamede", "Obafemi", "Damola","Duro","Ibrahim"]
firstName, secondName,thirdName,fourthName,fithName = input("Enter your name: "),input("Enter your name: "),input("Enter your name: "),input("Enter your name: "),input("Enter your name: ")
classNames.extend([firstName, secondName, thirdName,fourthName,fithName])
print(classNames.index(input("Search for a name: ")))
#  slicing doesn't give the end but the one before the last number if you want it to give you the last number then use 0:len(className) or [0:]
print(classNames[3:9:2])
# the third one like 2 is at a skip of one you can increase the skip sha

# should print 0-8 instead 