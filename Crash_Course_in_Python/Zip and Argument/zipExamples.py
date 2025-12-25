list1 = ['a','b','c']
list2 = [1,2,3]

#The following fuction will combine these two lists into a list of tuples -> [('a', 1), ('b', 2), ('c', 3)]
print("Zip Operation")
combinedList = [item for item in zip(list1, list2)]
print("Combined List: ",*combinedList)

#The following function will unzip the combined list
print("\nUnzip Operation")
letters, numbers = zip(*combinedList)
print("Letters: ", *letters)
print("Numbers: ", *numbers)

