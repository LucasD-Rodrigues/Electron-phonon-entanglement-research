from qutip import *
import numpy as np
import matplotlib.pyplot as plt
from hamiltonian import *
from target_states import *

up = basis(2,0)
down = basis(2,1)
ml_00 = tensor(basis(N,0),basis(N,0))
ch = tensor(coherent(N,alpha), coherent(N,alpha))

#prepare the state
psi0 = tensor(up,down,ml_00)
rho0 = ket2dm(psi0)
psi_coherent = tensor(up,down,ch)
rho_coherent = ket2dm(psi_coherent)

#dynamics

n=1000
T=5000

def f_dynamics():

    Fidelity = []
    times = np.linspace(0,T,n)

    __results__ = sesolve(H,psi_coherent,times)
    t_states = __results__.states

    for item in t_states:
        rho = ket2dm(item.unit())
        rho = item.ptrace([2,3])
        F = fidelity(rho,ket2dm(ch))
        Fidelity.append(F)

    print(max(Fidelity))
    plt.figure(figsize=(10,6))
    plt.xlabel("Time")
    plt.ylabel("Fidelity")
    plt.plot(times, Fidelity,label="fidelity of states")
    plt.grid()
    plt.legend()
    plt.show()

f_dynamics()

