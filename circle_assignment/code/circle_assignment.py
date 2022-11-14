#Python libraries for math and graphics

import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import random 
import subprocess
import shlex

import sys                                         
sys.path.insert(0,"/home/chandana/Downloads/fwc-main/CoordGeo")         

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

#if using termux
import subprocess
import shlex
#end if

I=np.eye(2)
e1=I[:,0]

#circle parameters
theta =90*np.pi/180
theta1=45*np.pi/180
theta2=30*np.pi/180
O=np.array(([0,0]))
r=1
A=np.array(([r*np.cos(theta2),r*np.sin(theta2)]))
B=np.array(([r*np.cos(theta2+theta),r*np.sin(theta2+theta)]))
M=np.array(([r*np.cos(2*theta1+2*theta),r*np.sin(2*theta1+2*theta)]))
M1=(A+B)/2
#circle
x_circ=circ_gen(O,r)
#circleplot
plt.plot(x_circ[0,:],x_circ[1,:],label='$Circles$')
tri_coords = np.vstack((A,B,O,M1)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','O','M1']
#Generating the line
m=-e1
k1=-10
k2=10
xAB=line_gen(A,B)
xOA=line_gen(O,A)
xOB=line_gen(O,B)
xOM1=line_gen(O,M1)
xBM=line_gen(B,M)
xAM=line_gen(A,M)
#Generating the circle 
x_circ1=circ_gen(O,r)
#plotting all the lines
plt.plot(xAB[0,:],xAB[1,:],label='Chord')
plt.plot(xOB[0,:],xOB[1,:],label='radius')
plt.plot(xOA[0,:],xOA[1,:],label='radius')
plt.plot(xOM1[0,:],xOM1[1,:],label='chord bisecter')
plt.plot(xAM[0,:],xAM[1,:],label='Chord')
plt.plot(xBM[0,:],xBM[1,:],label='Chord')
#labeling the coordinates
tri_coords = np.vstack((O,A,B,M1,M)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['O(0,0)','A','B','M1','M']
for i, txt in enumerate(vert_labels):
	plt.annotate(txt, # this is the text
        (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
        textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
   
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show() 
#plt.savefig('/sdcard/Download/c2_fwc/trunk/circle_assignment/docs/circle.png')
#subprocess.run(shlex.split("termux-open '/sdcard/Download/c2_fwc/trunk/circle_assignment/docs/main.pdf' "))
