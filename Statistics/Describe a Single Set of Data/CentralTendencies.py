from collections import Counter
from typing import List

num_friends = [100.0,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

#1. Mean(Average)
def mean(dataset: List[float]) -> float:
    return sum(dataset) / len(dataset)

#2. Median (Middle Value) - Changes on even sets and odd sets. So we define two separate functions and use them in a single function.
def _meanOdd(dataset: List[float]) -> float:
    #The list need to be sorted in order to get the mean value
    return sorted(dataset)[len(dataset)//2]

def _meanEven(dataset: List[float]) -> float:
    #The list need to be sorted in order to get the mean value
    sortedDataet = sorted(dataset)
    hi_midpoint = len(dataset)//2
    lo_midpoint = hi_midpoint - 1
    return (sortedDataet[lo_midpoint] + sortedDataet[hi_midpoint]) / 2