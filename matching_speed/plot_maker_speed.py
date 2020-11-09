import matplotlib.pyplot as plt 

# Code taken and adapted from:
# https://www.codespeedy.com/line-chart-plotting-in-python-using-matplotlib/
 
""" 
code for speed_plot.png
# Declaring the points for first line plot
x_axis = ["25k", "100k", "200k", "300k"]
Y1 = [0.06, 0.20, 0.38, 0.58] 
# plotting the first plot
plt.plot(x_axis, Y1, label = "cyac", color="red") 
# Declaring the points for second line plot
Y2 = [0.06, 0.23, 0.45, 0.68]
# plotting the second plot 
plt.plot(x_axis, Y2, label = "pyahocorasick", color="black") 
  
# Labeling the X-axis 
plt.xlabel('Hits') 
# Labeling the Y-axis 
plt.ylabel('Time in seconds') 
# Give a title to the graph
plt.title('Time taken to find hits(in AC automaton of 315k words)') 
"""

# Declaring the points for first line plot
x_axis = ["25k", "100k", "200k", "300k"]
Y1 = [50, 50, 50, 60] 
# plotting the first plot
plt.plot(x_axis, Y1, label = "cyac", color="red") 
# Declaring the points for second line plot
Y2 = [60, 60, 70, 70]
# plotting the second plot 
plt.plot(x_axis, Y2, label = "pyahocorasick", color="black") 
  
# Labeling the X-axis 
plt.xlabel('AC automaton patterns') 
# Labeling the Y-axis 
plt.ylabel('Time in milliseconds') 
# Give a title to the graph
plt.title('Time taken to find 25k hits(in AC automatons with different sizes)') 

# Show a legend on the plot 
plt.legend() 
 
plt.savefig("speed_25k_hits.png")