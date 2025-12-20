from collections import defaultdict
import re as regex

sentence = "Our Father, who art in heaven, hallowed be thy Name, thy kingdom come, thy will be done, on earth as it is in heaven. Give us this day our daily bread. And forgive us our trespasses as we forgive those who trespass against us. And lead us not into temptation but deliver us from evil. For thine is the kingdom, the power, and the glory for ever and ever. Amen."
words = regex.findall(r"\b\w+\b", sentence.lower())


wordCount = defaultdict(int)

for word in words:
    wordCount[word] += 1



#Accessing unavaiable values

print("Accessing unavaiable values: ",wordCount["Jesus"])