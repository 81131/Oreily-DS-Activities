list1 = [59,8,46,15,18,78,236,87]

#Normal form list[a:b:c]
# a-> Starting index (Inclusive)
# b-> Output index (Excluded)
# c-> Stride (Direction & Increment/ Decrement rate)

print(f"First Three ([:3]): {list1[:3]}")
print(f"Three to end ([3:]): {list1[3:]}")
print(f"One to four ([1:5]): {list1[1:5]}")
print(f"Without first and last ([1: -1]): {list1[1:-1]}")
print(f"First to last skipping one element after one [::2]: {list1[::2]}" )
print(f"Last to first with backward iteration [::-1]: {list1[::-1]}")

#Making a copy of list
print("\n\nMaking a copy of list: list2 = list1[:]")
list2 = list1[:]