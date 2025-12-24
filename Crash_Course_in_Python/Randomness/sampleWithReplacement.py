#This look just same as sample without replacement, but instead of sample we use choice. Same number can appear multiple times now.

import random

#Low Number Range = More likely to win
numRange = range(10)
positions = 6
lotteryNumbers = [random.choice(numRange) for _ in range(positions)]
winningNumbers = [random.choice(numRange) for _ in range(positions)]

print("Your lottery numbers are: ", *lotteryNumbers)
print("Winning numbers are: ", *winningNumbers)

#Congrats if you get at least 100 :) It's almost like a real life lottery 
def checkWinner(lotteryNumbers: list, winningNumbers: list): 
    winCount = 0
    moneyPool = 0
    for i,x in zip(lotteryNumbers, winningNumbers):
        if i == x:
            winCount +=1

    match winCount:
        case 6:
            moneyPool = 800000
        case 5: 
            moneyPool = 400000
        case 4:
            moneyPool = 20000
        case 3:
            moneyPool = 1000
        case 2:
            moneyPool = 500
        case 1:
            moneyPool = 100
        case 1:
            pass
    
    return winCount, moneyPool

winCount, moneyPool = checkWinner(lotteryNumbers, winningNumbers)
print(f"{winCount} numbers matched and you won ${moneyPool}!" if winCount>0 else "Sorry! No numbers matched")
