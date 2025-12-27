from collections import Counter
from matplotlib import pyplot as plt
grades = [83,95,91,97,70,0,85,82,100,67,73,77,0]

#Bucket grades by decile. but put 100 in with the 90s
histogram = Counter(min(grade//10*10, 90) for grade in grades)
#Returns a dict {0:2,10:0,...}

plt.bar([x+5 for x in histogram.keys()], #x axis: x+5 is the centre of the decile
        histogram.values(), #y axis
        width=10,
        edgecolor=(0,0,0))

plt.axis([-5,105, #x axis range
          0,5]) #y axis range

plt.xlabel("Decile")
plt.ylabel("# of students")
plt.title("Distribution of Exam 1 Grades")
plt.show()
