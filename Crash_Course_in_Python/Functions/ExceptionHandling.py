def divide (a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Can not divide by Zero!")
        return("\0")
    except TypeError:
        print("Invalid Input Type Provided!")
        return("\0")
    
#Example 01: No errors
print("\n\n\n")
print('No errors:print(divide(10,2))')
print(divide(10,2))


#Example 02: Zero division
print("\n\n\n")
print('Zero division: print(divide(10,0))')
print(divide(10,0))

#Example 03: Invalid Types
print("\n\n\n")
print('Invalid Types: print(divide("100", "ad"))')
print(divide("100", "ad"))
