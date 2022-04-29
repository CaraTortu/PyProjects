import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

# Get the amount of vectors
amount = int(input("How many vectors do you want to add?: "))
xValues = []
yValues = []

for i in range(amount):

    # Get the x and y values
    x = float(input("Enter the x-coordinate of vector {}: ".format(i+1)))
    y = float(input("Enter the y-coordinate of vector {}: ".format(i+1)))

    # Draw a vector with the given coordinates
    plt.arrow(0, 0, x, y, color='b', linewidth=1, head_width=0.1, head_length=0.25)
    plt.annotate(f'F{i+1}={x if abs(x)>abs(y) else y}N', xy=(x+0.3, y+0.3),xytext=(x+(0.3 if x >= 0 else -0.3), y+(0.3 if y >= 0 else -0.3)))
    xValues.append(x)
    yValues.append(y)

def truncate(n, decimals=0):
    # Truncates the given number to the given number of decimals
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

# Calculate the sum of the vectors
xyvalues = list(zip(xValues, yValues))

# Sort the values by their length
xValues.sort()
yValues.sort()

# Calculate the total force and display it
Tforce = np.sum(xyvalues, axis=0)
plt.arrow(0, 0, int(Tforce[0]), int(Tforce[1]), color='r', linewidth=1.5, head_width=0.2, head_length=0.4)
plt.annotate(f'|Ft|={truncate(sqrt((Tforce[0]**2)+(Tforce[1]**2)), 2)}N', xy=(int(Tforce[0])+0.3, int(Tforce[1])+0.3),xytext=(int(Tforce[0])+0.3, int(Tforce[1])+0.3))

# Display the plot
plt.xlim(xValues[-1]*(-1 if xValues[-1] > 0 else 1)-5, xValues[-1]*(-1 if xValues[-1] < 0 else 1)+5)
plt.ylim(yValues[-1]*(-1 if yValues[-1] > 0 else 1)-5, yValues[-1]*(-1 if yValues[-1] < 0 else 1)+5)
plt.show()