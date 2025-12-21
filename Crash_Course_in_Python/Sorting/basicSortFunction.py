unsortedList = [1,9,2,5,6,7,4,0,78]

sortedList = sorted(unsortedList) #unsortedList is not changed. sortedList is sorted. 

print("New List (New): ", *sortedList)
print("Original List (Not Intacted): ", *unsortedList)


unsortedList.sort() #This will sort the original unsortedList.
print("\nOriginal List (Sorted Now): ", *unsortedList) 
