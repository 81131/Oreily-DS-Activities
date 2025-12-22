#Enumerate is used to get BOTH index and value from a list/ generator or iterable object


names = ["Eleven", "Mike", "Will", "Max", "Dustin", "Lucas"]
print("Index\tName")
for index, name in enumerate(names): #Enumerate name return something like (index, name), (index, name)
    print(f"{index}\t{name}")

