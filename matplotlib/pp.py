import matplotlib.pyplot as plt
'''
# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Creating a simple plot
plt.plot(x, y)
plt.title('Simple Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()
x=[1,12,3,4,5]
y=[2,3,5,7,0]
# plt.plot(x,y,marker='o',linestyle='-',color='b',label='Circle marker')
# plt.plot(x,[i-1 for i in y],marker='D',linestyle='--',color='g',label='Triangle marker')
plt.plot(x,y,marker='o',linestyle='-',color='blue',label='Circle marker')
plt.plot(x,[i+3 for i in y],marker='D',linestyle='--',color='#ff7f0e',label='Triangle marker')
plt.title("Plot with different markers")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
#plt.grid(True)
# plt.grid(True,which='both',linestyle='--',linewidth=2,color='pink')
plt.grid(True,axis='x',linestyle='--',linewidth=1,color='black')
plt.grid(True,axis='y',linestyle='--',linewidth=1,color='pink')
plt.legend()
plt.show()

# import matplotlib.pyplot as plt
'''
# Sample data
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 5, 7, 11]
y2 = [1, 4, 9, 16, 25]

# Create a figure with multiple subplots
# plt.figure(figsize=(10, 5))

# First subplot (1 row, 2 columns, 1st plot)
plt.subplot(1, 2, 1)
plt.plot(x, y1, marker='o', color='blue')
plt.title('First Plot')
plt.xlabel('X')
plt.ylabel('Y1')

# Second subplot (1 row, 2 columns, 2nd plot)
plt.subplot(1, 2, 2)
plt.plot(x, y2, marker='s', color='green')
plt.title('Second Plot')
plt.xlabel('X')
plt.ylabel('Y2')

# Display the plots
plt.tight_layout()  # Adjusts the layout to prevent overlap
plt.show()

'''
import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Creating a scatter plot
plt.scatter(x, y)

# Adding titles and labels
plt.title('Simple Scatter Plot')
plt.xlabel('X Values')
plt.ylabel('Y Values')

# Display the plot
plt.show()

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
sizes = [20, 50, 80, 100, 150, 200, 250, 300, 350, 400]  # Sizes for the scatter points
colors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Colors for each point

# Creating a scatter plot with customization
plt.scatter(x, y, s=sizes, c=colors, alpha=0.7, edgecolor='black')

# Adding titles and labels
plt.title('Customized Scatter Plot')
plt.xlabel('X Values')
plt.ylabel('Y Values')

plt.grid(True)
plt.legend()
# Display the plot
plt.show()


import matplotlib.pyplot as plt

# Sample data
categories = ['A', 'B', 'C', 'D', 'E']
values = [5, 7, 3, 8, 4]

# Creating a bar graph
plt.bar(categories, values, color='skyblue')

# Adding labels and title
plt.title('Bar Graph Example')
plt.xlabel('Categories')
plt.ylabel('Values')

# Display the plot
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = np.random.randn(10)

# Creating a histogram
plt.hist(data, bins=5, color='lightgreen', edgecolor='black')

# Adding labels and title
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Display the plot
plt.show()
'''
'''
import matplotlib.pyplot as plt

# Sample data
labels = ['Python', 'Java', 'C++', 'JavaScript']
sizes = [35, 25, 20, 20]
colors = ['lightcoral', 'lightblue', 'lightgreen', 'yellow']
explode = (0, 0, 0, 0)  # "explode" the first slice

# Creating a pie chart
plt.pie(sizes, labels=labels, colors=colors, explode=explode, shadow=True)

# Adding a title
plt.title('Pie Chart Example')

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

# Display the plot
plt.show()
'''
'''
import matplotlib.pyplot as plt
import numpy as np

# Sample data
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# Creating a box plot
plt.boxplot(data, patch_artist=True, notch=True, vert=True)

# Adding a title
plt.title('Box Plot Example')
plt.xlabel('Dataset')
plt.ylabel('Value')

# Display the plot
plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
data = np.random.randn(100)  # 100 random data points from a normal distribution

# Creating a simple box plot
plt.boxplot(data)

# Adding a title
plt.title('Simple Box Plot')

# Display the plot
plt.show()

'''