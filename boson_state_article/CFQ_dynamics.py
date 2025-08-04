################################# Fidelity, Concurrence and Q Figures ###################################

from qutip import *
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
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

#define vectors
concurrences = []
Fidelity, Q_vals = [], []

delta1 = delta2

n = 1000

theta = np.pi*np.linspace(0,1,n)
times = theta/Omega0
x_axis = np.linspace(0,1,n)

psi0 = tensor(v10, v01, coherent(alpha=alpha, N=N), coherent(alpha=alpha, N=N))
rho0 = ket2dm(psi0)

b = destroy(N)
n_op = b.dag()*b

def MandelQ(rho):
    n = expect(n_op, rho)
    n2 = expect((n_op)**2, rho)

    if(n==0):
        Q = 0
    else:
        Q  = (n2 - n**2 - n) / n

    return Q

__result__ = sesolve(H(delta1), psi0, times,options=Options(nsteps=50000, atol=1e-10, rtol=1e-8)) 
t_states = __result__.states

for item in t_states:

    item = ket2dm(item.unit())

    C = concurrence(item.ptrace([0,1]))

    F = fidelity(item.ptrace(2), rho0.ptrace(2))

    Q_vals.append(MandelQ(item.ptrace(2)))
    Fidelity.append(F)
    concurrences.append(C)

plt.figure(figsize=(6,6))
plt.plot(x_axis,concurrences,label=r"Concurrence",linestyle="dashed",color="black")
plt.plot(x_axis,Fidelity,label=r"Fidelity to $\rho_{\alpha}$",color="blue")
plt.plot(x_axis,Q_vals,label=r"Mandel $Q$",color="red",linestyle="dotted")
plt.xlabel(r"$\theta$ (units of $\pi$)")
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()

        

