unsortedList = [-5,4,3,-2,-1,0,-10,-8]
sortedList = sorted(unsortedList, key=abs, reverse=True)

print("Sorted List: ", *sortedList)
#ABS -> Absolute value. (Ex: -10 abs value = 10)
#Therfore abs sorted version is [10 8 5 4 3 2 1 0]. But the output will be [-10 -8 -5 4 3 -2 -1 0]