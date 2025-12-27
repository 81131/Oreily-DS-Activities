from matplotlib import pyplot as plt

IQs = {"Christoper Hirata": 225, "Terence Tao": 230}

#This bar chart shoes the IQ difference as a huge difference
plt.bar(IQs.keys(),
         IQs.values(),
         )

plt.axis([-0.5,1.5,224,232])
plt.title("Really Inconvenient Way to show IQ")
plt.xlabel("Scientist")
plt.ylabel("IQ Score")
plt.show()

#This bar chart shoes the IQ difference in an acceptable way
plt.bar(IQs.keys(),
         IQs.values(),
         )

plt.axis([-0.5,1.5,0,240])
plt.title("Much more convenient Way to show IQ")
plt.xlabel("Scientist")
plt.ylabel("IQ Score")
plt.show()