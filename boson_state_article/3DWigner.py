####################################### 3D Plot - Wigner Function #######################################

from qutip import *
import numpy as np
from total_hamiltonian import *
import matplotlib.pyplot as plt

xmax = 5
points = 200
t = 500

#simulation parameters
n = 1000
theta = np.pi*np.linspace(0,0.1,n)
times = theta/Omega0
x_axis = np.linspace(0,0.1,n)

psi0 = tensor(v10,v01,coherent(alpha=alpha, N=N), coherent(alpha=alpha,N=N))
#psi0 = Bell1

#dynamics
__result__ = sesolve(H, psi0, times,options=Options(nsteps=50000, atol=1e-10, rtol=1e-8)) 
state = __result__.states[t]
state = ket2dm(state.unit()).ptrace(2)
#state = coherent(N,alpha)
# Generate phase space grid
xvec = np.linspace(-xmax, xmax, points)
X, Y = np.meshgrid(xvec, xvec)

# Compute Wigner function
W = wigner(state, xvec, xvec)

# 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, W, cmap='RdBu_r', edgecolor='none')

ax.set_title(f'3D Wigner Function for α = {alpha}')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('W(X, Y)')

plt.tight_layout()
plt.show()