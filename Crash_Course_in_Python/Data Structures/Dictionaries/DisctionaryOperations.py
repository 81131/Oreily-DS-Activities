#Checking existence of a value
dict1 = {"Name": "Dinindu", "Age": 21}

def checkValExistence(dictName: dict, value: object) -> str:
    print ( "Value exist" if value in dictName.values() else "Value does not exist")

#Valid value
print("\n\nValid Value Check:")
checkValExistence(dict1, "Dinindu")

#Invalid value
print("\n\nInvalid Value Check:")
checkValExistence(dict1, "John")

#get operator

#Valid value
print("\n\nValid Value Check:")
print(dict1.get("Name",0))

#Invalid value
print("\n\nInvalid Value Check:")
print(dict1.get("Address",0))

