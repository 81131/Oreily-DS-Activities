#Comprehensation basically means deriving some value from one another
#Here we are deriving square of the even numbers using original even numbers
evenNumbers = [x for x in range(10) if x % 2 == 0]
evenSquares = [x * x for x in evenNumbers]

print("Even numbers: ", *evenNumbers)
print("Even Squares: ", *evenSquares)