#Defining sets
set1 = set()
set2 = {1,2,3}

#Adding elements
set1.add(10)
set1.add(20)
set1.add(20) #Will execute but won't be stored as a separate value. Sets only stores unique value

print("Set1 Values: ", *set1)


#Removing element (Can not take index. Only the value itself)
set2.remove(2)

print("\n\nSet2 Values: ", *set2)