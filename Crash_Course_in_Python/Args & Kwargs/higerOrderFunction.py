def doubler(f):
    def g(x):
        return 2*f(x)
    
    #This returns a literal function. This is not equal to calling g()
    return g


def f1(x):
    return x + 1 

#We catch that function here. Now g itself is a function --> doubler(x+1)
g = doubler(f1)

#And we pass value 3 
print(g(3))

#This will g(2*(f1(x))) --> g(2*(3+1)) = 8
