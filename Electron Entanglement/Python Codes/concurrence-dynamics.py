from qutip import *
import matplotlib.pyplot as plt
import numpy as np
import math
from total_hamiltonian import *

#define constant
concurrences = []

omega = 20*10**-3
Delta = 5*(10**-3)*omega
g = 0.1*omega
delta2 = 0.1*omega #tunned to either 0 or 0.1
alpha = g/omega
delta1 = delta2
Omega0 = 2*Delta**2/omega

n = 1000

theta = math.pi*np.linspace(0,1,n)
times = theta/Omega0
x_axis = np.linspace(0,1,n)

rho0 = ket2dm(ud)

def c_dynamics():
    __result__ = sesolve(H(delta1), ud, times,options=Options(nsteps=50000, atol=1e-10, rtol=1e-8)) 
    t_states = __result__.states

    for item in t_states:

        item = ket2dm(item).ptrace([0,1])
        C = concurrence(item)

        concurrences.append(C)

    plt.plot(x_axis,concurrences,label="concurrence",color="black")
    plt.title("Dynamic Concurrence")
    plt.ylabel("Concurrence")
    plt.xlabel("Theta (units of pi)")
    plt.show()
        

c_dynamics()

