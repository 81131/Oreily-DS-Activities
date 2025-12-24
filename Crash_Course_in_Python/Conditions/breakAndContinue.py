marksAndGrade = {"Ned": 98, "Jon": 87, "Arya": 95, "Sansa": 80, "Catelyn": 90, "Robb": 92, "Bran": 86, "Rickon": 97, "END":2500}
Juniors = ["Jon", "Arya", "Sansa", "Bran", "Rickon", "Robb"]

print("This will print the marks of Stark Family kids - excluding parents")
for name,marks in marksAndGrade.items():
    if name == "END":
        break
    if name not in Juniors:
        continue
    print(f"{name}: {marks}")
