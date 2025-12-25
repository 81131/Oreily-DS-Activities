def finalMarkCalculator(name,midMark,finalMark) -> None: 
    print("Name\t\tMarks")
    print(f"{name}\t{midMark + finalMark}")

studentMarks = {"name": "Hermione", "mid": 50, "final":50}

#This will unpack the ["Hermione",50,50] and give -> "Hermione",50,50
finalMarkCalculator(*studentMarks.values())