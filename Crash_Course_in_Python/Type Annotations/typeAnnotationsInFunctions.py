#num1: int means num1 should be an integer
#num2: int means num2 should be an integer
# -> int means the function will return an integer
#Even though we define this, Python will still accept other values (float, str, etc.) as inputs.
def add(num1: int, num2:int) -> int:
    return num1 + num2

print(add(10,20)) #Output: 30
print(add("Hello", " World!")) #Output (Python 3.6 or later): Hello World! 
print(add(10.5, 11.25)) #Output: 21.75

#So, mostly type annotations are useful for IDE support (It will display dictionary options, String manipulation options, etc.)and documentation pusposes.