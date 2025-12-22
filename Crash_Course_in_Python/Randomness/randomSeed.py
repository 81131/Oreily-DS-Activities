import random

random.seed(10) #A seed is used in case if we need to get the same result every time. Mostly used for developement purposes. 

two_random_nums = [random.random() for _ in range(2)]

print("Random Numbers:", *two_random_nums)
#this will always print -> Random Numbers: 0.5714025946899135 0.4288890546751146