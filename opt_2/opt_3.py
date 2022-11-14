import matplotlib.pyplot as plt
import numpy as np
import cvxpy  as cp
from cvxpy import *
#if using termux
import subprocess
import shlex
#end if
V = np.array(( [0,0.5], [0.5, 0]))
u = np.array([0,0]).reshape(2,1)
f=1
X=cp.Variable((2,2),symmetric=True)
# objective function coeffs
c = np.array([1.0, 1.0])
x = cp.Variable((2,1),nonneg=True)
# function
F=c@x
obj = Minimize(F)
#Constraints
constraints = [
	trace(V @ X==0),
]


#solution
prob = Problem(obj, constraints)
prob.solve()
print("status:", prob.status)
print("optimal value:", F.value)


#if using termux
#plt.savefig(os.path.join(script_dir, fig_relative))
#subprocess.run(shlex.split("termux-open "+os.path.join(script_dir, fig_relative)))
#else
plt.show()
