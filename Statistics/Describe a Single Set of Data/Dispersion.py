#Dispersion is a measure about how spread the dataset is

from collections import Counter
from typing import List
import math
num_friends = [100.0,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]


#PREVIOUS FUNCTIONS NEEDED TO SOME NEW FUNCTIONS
#------------------------------------------------
def mean(dataset: List[float]) -> float:
    """Returns the mean of provided dataset"""
    return sum(dataset) / len(dataset)
#------------------------------------------------




#1. Range (The max - min)
def data_range(dataset: List)-> float:
    """Returns the range of the given dataset"""
    return max(dataset) - min(dataset)


#2. Variance (Measure for the spread of data points from the mean)
#Formula = s² = Σ (xᵢ - x̄)² / (n - 1)
#Helper function to get the datapoint - mean
def _mean_dif(dataset: List[float]) -> float:
    """Translates the datapoints in the provided dataset to [(value_i - mean),..., (value_n - mean)]"""
    meanVal = mean(dataset)
    return [datapoint - meanVal for datapoint in dataset]

#Helper function to get sum of squares
def sum_of_squares(inputList: List[float]) -> float:
    """Returns the sum of squares of for a given list"""
    return sum(x**2 for x in inputList)

def variance(dataset: List) -> float:
    """Returns the variance for a given list"""
    deviations = _mean_dif(dataset)
    n = len(dataset)
    return sum_of_squares(deviations) / (n-1)


#3. Standard Deviation (This is the square root of the variance)
def standard_deviation(dataset: List) -> float: 
    """Returns the standard deviation for a given list"""
    return math.sqrt(variance(dataset))