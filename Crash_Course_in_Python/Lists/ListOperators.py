# In operator (Use to check availability of an element)
list1 = [59,8,46,15,18,78,236,87]
print(f"Original List: {list1}")
print(f"Check if 18 available in list1 ('Yes' if 18 in list1 else 'No'): {'Yes' if 18 in list1 else 'No'}")
print(f"Check if 10 available in list1 ('Yes' if 10 in list1 else 'No'): {'Yes' if 10 in list1 else 'No'}")


#Extend Operator
print(f"\n\nOriginal List: {list1}")
print(f"list1.extend([78,59,45])")
list1.extend([78,59,45])
print(f"Extended List: {list1}")


#Extend Without Modifying the Original List
list1 = [59,8,46,15,18,78,236,87]
print(f"\n\nOriginal List: {list1}")
print(f"list2 = list1 + [78,59,45]")
list2 = list1 + [78,59,45]
print(f"Extended List: {list2}")
print(f"Original List: {list1}")

# Append Items
print("\n\nAppending Items")
print(f"Original List: {list1}")
list1.append(92)
print(f"list1.append(92)")
print(f"List after appending: {list1}")


#Unpacking a list
print(f"\n\nx, y = [100,500]")
x, y = [100,500]
print(f"x = {x}\ny= {y}")

