#

def generate_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

data = generate_range(20)

#These two won't do anything if is wann't for loop. Basically for loop is picking next() value from the generator object.
evens = (x for x in data if x%2 == 0)
even_squares = (x ** 2 for x in evens)

print(*even_squares)