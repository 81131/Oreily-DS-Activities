post = {
    "user": "81131",
    "email": "81131@example.com",
    "title": "Data Science is easy 🤥",
    "reactions": {"love": 10, "care": 2, "haha": 12},
    "share_count": 23,
    "hashtags": ["meme", "funny", "datascience", "coding"]

}

#Keys
keySet = post.keys()
print("Keys: ", *keySet)


#Values
valueSet = post.values()
print("Values: ", *valueSet)

#Items (Key, Value tuple)
itemSet = post.items()
print("Items: ", *itemSet)
