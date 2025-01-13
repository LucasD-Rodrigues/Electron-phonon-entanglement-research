from qutip import *
import numpy as np
import matplotlib.pyplot as plt
from cts import *

#defining first bosonic space
N = 13
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

#electron hamiltonian
H0 = delta1*1/2*tensor(sigmaz(), qeye(2), qeye(N), qeye(N)) + 1/2*delta2*tensor(qeye(2), sigmaz(), qeye(N), qeye(N))

#tunneling hamiltonian
Ht = Delta*tensor(sigmax(), qeye(2), qeye(N), qeye(N)) + Delta*tensor(qeye(2), sigmax(), qeye(N), qeye(N) )

H = H0 + Ht + H_V + V_DV