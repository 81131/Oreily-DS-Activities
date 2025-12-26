from matplotlib import pyplot as plt

movies = [
    "12th Fail", 
    "Spider-Man: Across the Spider-Verse", 
    "Oppenheimer", 
    "Godzilla Minus One", 
    "The Holdovers", 
    "Guardians of the Galaxy Vol. 3", 
    "Poor Things", 
    "Past Lives", 
    "Anatomy of a Fall", 
    "John Wick: Chapter 4"
]

ratings = [8.9, 8.6, 8.3, 8.3, 7.9, 7.9, 7.9, 7.8, 7.7, 7.7]

plt.bar(movies, ratings, color = "red")
plt.title("Best Movies - 2025")
plt.ylabel("IMDB Rating")
plt.xlabel("Movie name")
plt.xticks(movies, rotation = 90)
plt.tight_layout()
plt.show()