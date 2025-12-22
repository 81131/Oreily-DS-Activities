#A list for generate number could be inconvenient as it stores numbers generates in the memory. To save memory we can use generators

def generate_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

for i in generate_range(5):
    print(f"i: {i}")