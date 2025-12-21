#If elseone line

def maxNum(x:int, y:int):
    print( f"{x} is larger than {y}" if x>y  else f"{y} is larger than {x}" if  y>x   else f"{x} and {y} are even")

maxNum(10,20)
maxNum(20,20)
maxNum(15,5)