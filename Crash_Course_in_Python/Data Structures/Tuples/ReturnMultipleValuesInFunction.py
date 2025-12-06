def addAndMultiply(a,b):
    try:
        return (a+b), (a*b)
    except TypeError:
        print("Make sure to enter the numeric values!")
        return None, None
    except Exception as err:
        print(f"Error occurred. This log may help: {err}")
        return None, None

x,y = addAndMultiply(10,2)
print(f"Sum: {x}\nProduct: {y}")