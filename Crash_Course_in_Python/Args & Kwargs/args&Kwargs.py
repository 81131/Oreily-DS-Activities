def multiArgPrinting(*args, **kwargs): #Args just means arguments, while kwargs means keyword arguments
    print("Unnamed arguments: ",args)
    print("Keyword Arguments: ", kwargs)

#This demonstrate the multiple arguments unpacking. The * will unzip the unnamed arguments while ** unzip the keyword arguments
multiArgPrinting(10,20,30,name = "Dinindu", userName = "81131", password = "You really thought I'll just type it out in a public repo?")

print("\n")
#Instead of that, we can also pass the unzipped arguments directly. 
def adder(a,b,c):
    print("Sum", (a+b+c))

numList = [10,20]
numDict = {"c":30} #Be careful. We must use the same variable name (c) we used in the function here 

#Just think of * as a way to unzip a list and ** a way to unzip a dict
adder(*numList, **numDict)