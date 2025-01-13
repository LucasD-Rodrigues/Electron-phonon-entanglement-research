#Hamiltonian QD - boson system

from qutip import *
import matplotlib.pyplot as plt
import numpy as np

#define constant
omega = 20*10**-3
Delta = 5*10**-3*omega
g = 0.1*omega
delta2 = 0.1*omega #tunned to either 0 or 0.1
alpha = g/omega

#defining first bosonic space
N = 13 #truncating the basis at m = l = 13
b1 = tensor(qeye(2), qeye(2), destroy(N), qeye(N))

#defining second bosonic space
b2 = tensor(qeye(2), qeye(2), qeye(N), destroy(N))

#boson hamiltonian 
H_V = omega*(b1.dag()*b1 + b2.dag()*b2)

#fermionic operators
N1 = tensor(sigmam()*sigmap(), qeye(2), qeye(N), qeye(N))
N2 = tensor(sigmap()*sigmam(), qeye(2), qeye(N), qeye(N))
N3 = tensor(qeye(2), sigmam()*sigmap(), qeye(N), qeye(N))
N4 = tensor(qeye(2), sigmap()*sigmam(), qeye(N), qeye(N))

#interaction
V_DV = g*(N1 + N3)*(b1.dag() + b1) + g*(N2 + N4)*(b2.dag() + b2)

Delta_list = np.linspace(-0.2,0.2,100)  # consider delta1 varying (fixed for concurrence analysis)

#define Hamiltonian
def H(delta1):

    HT = delta1*1/2*tensor(sigmaz(), qeye(2), qeye(N), qeye(N)) + 1/2*delta2*tensor(qeye(2), sigmaz(), qeye(N), qeye(N)) + Delta*tensor(sigmax(), qeye(2), qeye(N), qeye(N)) + Delta*tensor(qeye(2), sigmax(), qeye(N), qeye(N) ) + H_V + V_DV

    return HT

#general computational basis

#fermions
v10 = basis(2,0)
v01 = basis(2,1)

#bosons
m = basis(13,0)
l = basis(13,0)

uu = tensor(v10,v10,m,l)
ud = tensor(v10,v01,m,l)
du = tensor(v01,v10,m,l)
dd = tensor(v01,v01,m,l)
