import matplotlib.pyplot as plt
import sys
sys.path.insert(0, '/home/nithink/matgeo/codes/CoordGeo') 
import numpy as np
import matplotlib.pyplot as plt

from line.funcs import *

def customize_plot():
    """
    Customizes the plot by setting the position of the axes, removing top and right spines,
    and enabling grid with equal axis scaling.
    """
    ax = plt.gca()#to generate current axes
    ax.spines['top'].set_color('none')#makes the top spine invisible
    ax.spines['left'].set_position('zero')#repositions the left axis at x=0
    ax.spines['right'].set_color('none')#makes the top spine invisible
    ax.spines['bottom'].set_position('zero')#repositions the bottom axis at y=0

    # Uncomment the following lines if you want to add labels to the axes
    #plt.xlabel('$x$')
    #plt.ylabel('$y$')
    
    plt.legend(loc='best')#adds legend to the plot and loc='best' automatically chooses the location that minimizes overlap with the actual plot elements
    plt.grid(True)#shows the grid
    plt.axis('equal')#ensures each unit on the x-axis is equal to that on y-axis


def plot_points(points, labels):
    """
    Plots the given points and labels them with their coordinates.
    
    Parameters:
    - points: A 2D array where each column is a point in 2D space.
    - labels: A list of labels corresponding to each point.
    """
    # Scatter plot of the points
    plt.scatter(points[0, :], points[1, :])

    # Label each point with its respective label and coordinates
    for i, label in enumerate(labels):
        plt.annotate(f'{label}\n({points[0, i]:.0f}, {points[1, i]:.0f})',
                     (points[0, i], points[1, i]), # Position of the label
                     textcoords="offset points", # How to position the text
                     xytext=(20, 5), # Distance from text to points (x, y)
                     ha='center') # Horizontal alignment can be left, right, or center



def plot_line(P, Q):
    x_PQ = line_gen(P,Q)#GVV function

    # Plot the line
    plt.plot(x_PQ[0, :], x_PQ[1, :], label=f'Line from ({P[0]}, {P[1]}) to ({Q[0]}, {Q[1]})')#plots the x and y coordinates in X_AB

data = np.genfromtxt('values.dat', delimiter=' ', names=True)
x = data['x']
y = data['y']
P = np.array(([x[0], y[0]])).reshape(-1,1)
Q = np.array(([x[1], y[1]])).reshape(-1,1)
plot_line(P, Q)
points = np.block([[P, Q]])
labels = ['A', 'B']
plot_points(points, labels)
customize_plot()
plt.show()
