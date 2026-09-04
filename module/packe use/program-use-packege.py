import matplotlib.pyplot as plt

x = [12,14,15,18,19,25,]
y = [12,14,15,18,19,25,]

plt.bar(x, y, label = "Bar Data")

plt.scatter(x, y, label = "Scatter Points")

plt.xlabel("X Axis")
plt.ylabel("Y Axix")
plt.title("Simple Bar + Scatter Points")

plt.legend()
plt.show()