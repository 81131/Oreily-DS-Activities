from collections import Counter

c = Counter([10,1,2,10])

print(*(c.items()))

#Example - Number of time ten appears
print("Ten Count: ", c[10])