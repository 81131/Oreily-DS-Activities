#Basically Assertion error are developer made rules which will throw an error message if broken. They are used to 
#For an example lets say we want to check the functionality of a min - max function. 

def MaxFinder (num1: int, num2: int):
    if num1 < num2:
        return num1
    else:
        return num2

#Clearly the function iswrong, but yet it execute. So we will add kind of a test subject to verify the functionality. 
assert MaxFinder(10,20) == 20, "Test with 10 vs 20 -> The 20 is larger but function did not get it correct"