list1 = [48,59,67]
tuple1 = (48,59,67)

print(f"Original List: {list1}\nOriginal Tuple: {tuple1}")

def changeFirstElement(x, y):
    try:
        x[0] = y
    except Exception as err: 
        print(f"Error Occurred: {err}")

#Try mutating the list
print(f"\n\nTry mutating the list")
print(f"Original List: {list1}")
print(f"list1[0] = 10: {changeFirstElement(list1, 10)}")
print(f"After Mutating List: {list1}")

#Try mutating the tuple
print(f"\n\nTry mutating the tuple")
print(f"Original Tuple: {tuple1}")
print(f"tuple[0] = 10: {changeFirstElement(tuple1, 10)}")
print(f"After Attempt Mutating Tuple: {tuple1}")
