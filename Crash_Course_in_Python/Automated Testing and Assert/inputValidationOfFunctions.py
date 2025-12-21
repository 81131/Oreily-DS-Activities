def smallestItem(inputList: list):
    #Empty list -> False. Therefore if empty list provided function will throw an assertion error. 
    assert inputList, "Empty list provided. Therefore no smallest items" 
    
    print("Minimum Value: ",min(inputList))


validList = [1,2,3,5,8,9,7,5,95,87,646,151,875,785]
invalidList = []

print("Valid Input: ")
smallestItem(validList)

print("\nInvalid Input")
smallestItem(invalidList)
