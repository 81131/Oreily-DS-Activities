evenNumbers = [x for x in range(10) if x % 2 == 0]
squaredEven = {x: x*x for x in evenNumbers}

print("Number\t Square")
for num, sqr in squaredEven.items():
    print(f"{num}\t {sqr}")