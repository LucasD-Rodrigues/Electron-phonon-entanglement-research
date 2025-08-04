################################### Texture Quantification -Rugosity ####################################

from qutip import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from total_hamiltonian import *

#setting up LaTex plot
rcParams.update({
    "text.usetex": True,
    "font.family": "serif",  # or 'sans-serif' for a modern look
    "font.serif": ["Computer Modern Roman"],  # default LaTeX font
    "axes.labelsize": 16,    # LaTeX font size
    "font.size": 15,
    "legend.fontsize": 15,
    "xtick.labelsize": 16,
    "ytick.labelsize": 16
})

#function to compute the state rugosity
def Rugosity(rho):

    grand_sum = np.sum(rho.full())
    R = -np.log(grand_sum)

    return R

delta1 = delta2 #setting up delta parameter
n = 1000

#dynamic parameters of the system
theta = np.pi*np.linspace(0,1,n)
times = theta/Omega0
x_axis = np.linspace(0,1,n)

#initial unevolved state
psi0 = tensor(v10, v01, coherent(alpha=alpha, N=N), coherent(alpha=alpha, N=N))

#dynamic equation numerical solving
__result__ = sesolve(H(delta1), psi0, times,options=Options(nsteps=50000, atol=1e-10, rtol=1e-8)) 
t_states = __result__.states

R_vec = []

#calculating and plotting rugosity
for state in t_states:
    state_dm = ket2dm(state.unit()).ptrace(2)
    R_vec.append(Rugosity(state_dm))

plt.plot(x_axis, R_vec, color="blue")
plt.grid(True)
plt.xlabel(r"$\theta$ (units of $\pi$)")
plt.ylabel(r"State Rugosity $R(\rho)$")
plt.show()

#entanglement correlation test
beta1 = np.array([state*b1*state])