# Code by GVV Sharma
# June 12, 2022
# Revised November 14, 2023
# Released under GNU GPL

# Drawing a pair of tangents to a conic

import sys  # for path to external scripts
sys.path.insert(0, '/home/nithink/matgeo/codes/CoordGeo')  # path to my scripts
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

# local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import *

# radius
r = 2

# Given Points
#B = np.array(([2, 4])).reshape(-1, 1)
#A = np.array(([2, -4])).reshape(-1, 1)  # Reshaping A as a column vector
V = np.eye(2)
#h = A
u = np.array(([0, 0])).reshape(-1, 1)  # Reshaping u as a column vector
f = -4

# Generating circle
x_circ = circ_gen(-u, r)

# Finding points of contact
#[B, C] = contact(V, u, f, h)
#D = np.array(([0, 4])).reshape(-1, 1)
#C = np.array(([0, -4])).reshape(-1, 1)
#x_A = line_gen(B,A)  # Line generated from point A
#x_B = line_gen(C,D)  # Line generated from point B

# Plotting all lines
#plt.plot(x_A[0, :], x_A[1, :], label='$x = 2$')
#plt.plot(x_B[0, :], x_B[1, :], label='$x = 0$')
n1 = np.array(([1, 0])).reshape(-1,1) 
c1 = 0
n2 = np.array(([1, 0])).reshape(-1,1)
c2 = 2
k1 = -4
k2 = 4
#Generating Lines
x_A = line_norm(n1,c1,k1,k2)
x_B = line_norm(n2,c2,k1,k2)
plt.plot(x_A[0,:],x_A[1,:],label='$x = 0$')
plt.plot(x_B[0,:],x_B[1,:],label='$x = 2$')
colors = np.arange(1,4)
#tri_coords = np.block([[A,B,C]])
#plt.scatter(tri_coords[0,:], tri_coords[1,:], c=colors)
#vert_labels = ['A','B','C']
#for i, txt in enumerate(vert_labels):
    #plt.annotate(txt, # this is the text
    #plt.annotate(f'{txt}\n({tri_coords[0,i]:.2f}, {tri_coords[1,i]:.2f})',
                 #(tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 #textcoords="offset points", # how to position the text
                 #xytext=(25,5), # distance from text to points (x,y)
                 #ha='center') # horizontal alignment can be left, right or center

# Plotting all lines and circles
plt.plot(x_circ[0, :], x_circ[1, :], label='$Circle$')

# Adjusting axis spines
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

# Define the space
x = np.linspace(0,2,100)
y_circle = np.sqrt(4-x**2)


# Fill the area between the lines and the circle
plt.fill_between(x,0, y_circle, color='red', alpha=0.5, label='Shaded Region')

# Labels and title
plt.xlabel('x')
plt.ylabel('y')

# Display the plot
# Final plot settings
plt.legend(loc='upper right')
plt.axis('equal')
plt.show()
