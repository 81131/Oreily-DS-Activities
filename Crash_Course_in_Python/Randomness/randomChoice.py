import random
def randomUserName(firstNameList : list, lastNameList : list):
    firstName = random.choice(firstNameList)
    lastName = random.choice(lastNameList)
    return firstName + " " + lastName

firstNameList = ["Awesome", "Generous", "Kind", "Worthy"]
lastNameList = ["Opponent", "Friend", "Gaur", "Phoenix"]

#This will print something like "Worthy Phoenix"
print("Welcome! Your user name is: ", randomUserName(firstNameList, lastNameList))
