#Creating empty dictionaries
emptyDict1 = {}
emptyDict2 = dict()

#Dictionary with values
dict1 = {"Name": "Dinindu", "Age": 21}

#Aceesing a value
print(f"Name: {dict1["Name"]}")

#Handling key value errors
def printFromDict(dictName: dict, index: object):
    try:
        print(dictName[index])
    except KeyError:
        print("The key value does not exist!")
    except Exception as err:
        print(f"Error occurred. Please read the log here: {err}")



#Valid value
print("\n\nValid Key Value:")
printFromDict(dict1, "Name")

#Inalid value
print("\n\nInvalid Key Value:")
printFromDict(dict1, "John")

#Invalid Dictionary
print("\n\nNon Integer Index:")
printFromDict(dict1, [0.256,58,987])