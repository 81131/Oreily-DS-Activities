#First Class Behavior: functions are treated like any other variable
def double(x):
    """
    This is where you put an optional docstring that explains what the
    function does. For example, this function multiplies its input by 2.
    """
    return x * 2

def apply_to_one(f):
    """Calls the function f with 1 as its argument"""
    return f(1)

my_double = double             # refers to the previously defined function
x = apply_to_one(my_double)    # equals 2

#Lambda functions: small anonymous functions defined with the lambda keyword
y = apply_to_one(lambda x: x + 4)  # equals 5



