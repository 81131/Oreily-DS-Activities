from matplotlib import pyplot as plt

friends = [8,5,7,4,6,3,5,9,9]
minutes = [140,210,180,120,160,90,150,200,195]

labels = ["Harry", "Hermione", "Ron", "Draco", "Luna", "Neville", "Ginny", "Fred", "Geoege"]


plt.scatter(minutes, friends)

for label, friend_count, minutes_in_common_room in zip(labels, friends, minutes):
    plt.annotate(label,
                 xy=(minutes_in_common_room, friend_count),
                 xytext=(5, -5),
                 textcoords="offset points")

plt.ylabel("Number of Friends")
plt.xlabel("Time Spent in the common room")
plt.title("Time spent in the common room vs Friends")

plt.show()