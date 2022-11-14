#Code by GVV Sharma (works on termux)
#March 19, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#Algo from Wikipedia
#Solving a mensuration optimization problem using 
#Gradient Descent

#Python libraries for math and graphics
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
from pylab import *


import sys                                         
sys.path.insert(0,'/sdcard/Download/c2_fwc/trunk/CoordGeo')        
#local imports
from line.funcs import *
from triangle.funcs import *
#from conics.funcs import circ_gen
from conics.funcs import *

#if using termux
import subprocess
import shlex
#end if

def f(x):
	return  x+1/x


#Gradient Descent
cur_x = 1 # The algorithm starts at x=2
gamma = 0.001 # step size multiplier
precision = 0.00000001
previous_step_size = 1 
max_iters = 100000000 # maximum number of iterations
iters = 0 #iteration counter

df = lambda x: (x**2-1)/x**2


while (previous_step_size > precision) & (iters < max_iters):
    prev_x = cur_x
    cur_x -= gamma * df(prev_x)
    previous_step_size = abs(cur_x - prev_x)
    iters+=1
min_val=f(cur_x,)
print("Minimum value of f(x) is ", min_val, "at","x =",cur_x)

label_str = "$x+Y$"
#Plotting f(x)
x=np.linspace(0.1,10,100)
y=f(x)
plt.plot(x,y)
#Labelling points
plt.plot(cur_x,min_val,'o')
plt.text(cur_x, min_val,f'P({cur_x:.4f},{min_val:.4f})')

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
#plt.legend()
plt.savefig('/sdcard/Download/c2_fwc/trunk/opt_1/docs/opt.pdf')
subprocess.run(shlex.split("termux-open '/sdcard/Download/c2_fwc/trunk/opt_1/docs/opt_2.pdf'")) 
plt.show() 
