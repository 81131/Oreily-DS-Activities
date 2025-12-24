import re as regex

#Check for a letter
word = "cat"
searchFor = "b"
print("Check for a letter")
print("Found Result" if regex.search(searchFor, word) else "Not Found!")

#Check for a match
word = "dogsarebetterthancats"
searchFor = "dog"
print("\nCheck if sentence start with word ~dog~")
print("Yes" if regex.match(searchFor, word) else "No")

#Split on a specific letter/ word
print("\nSplit the word on ~dd~ and pass them to a list")
word = "Thisddmessageddisddnotddvisibleddyet!"
decrypted = regex.split("dd", word)
print("Decrypted Message: ", *decrypted)

#Replace letters
print("\nReplace a letter with regular expressions")
word = "I really need a bug right now"
print(regex.sub("b", "h", word))

