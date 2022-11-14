#Code by GVV Sharma (works on termux)
#March 19, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#Solving a differential calculus problem using cvxpy and geometric programming


#Python libraries for math and graphics
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
from pylab import *
import cvxpy  as cp


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

#Declaring Variables
x = cp.Variable(pos=True, name="x")
y = cp.Variable(pos=True, name="y")

#objects
#minimum value of the function
f = x+y

#constraints
constraints = [
        x*y == 1.0
]

#Problem Formulation
problem = cp.Problem(cp.Minimize(f), constraints)

#Checking cuvature of the objective function
print(f.log_log_curvature)

#Checking if the problem is DGP
print("Is this problem DGP?", problem.is_dgp())


#solution
problem.solve(gp=True)
print("the minimum  value of the x",x.value)
print("the minimum value of y",y.value)
subprocess.run(shlex.split("termux-open '/sdcard/Download/c2_fwc/trunk/opt_1/docs/opt_1.pdf' ")
print("therefore")

print("the minimum value of the function",problem.value)


