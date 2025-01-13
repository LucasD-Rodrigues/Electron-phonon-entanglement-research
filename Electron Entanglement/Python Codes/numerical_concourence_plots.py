from qutip import *
import matplotlib.pyplot as plt
import numpy as np
from total_hamiltonian import *

Delta_list = np.linspace(-0.2,0.2,1700)  # consider delta1 varying

#concurrence function
def concurrence_by_dm(n):

    concurrence_list = []
    vecs_list = []
    v = [] #empty state vector
    
    #eigenstates for every possible numerical delta1
    for delta1 in Delta_list:

        vals, vecs = H(delta1).eigenstates() 

        vecs_list.append(vecs)

    #extracting only |v> states
    for i in range(len(Delta_list)):

        v.append(vecs_list[i][n]) #fixed state with delta changing

    for item in v:
        rho = ket2dm(item).ptrace([0,1]) #tracing over the qubits
        C = concurrence(rho) 
        concurrence_list.append(C) #concurrence of the state v for every delta1

    concurrence_list = np.array(concurrence_list)

    return concurrence_list

#plotting results

plt.plot(Delta_list, concurrence_by_dm(0),label="Eigenstate 1",color="black")
plt.plot(Delta_list, concurrence_by_dm(1),label="Eigenstate 2",color="black",linestyle="dashed")
plt.plot(Delta_list, concurrence_by_dm(2),label="Eigenstate 3",color="rosybrown")
plt.plot(Delta_list, concurrence_by_dm(3),label="Eigenstate 4",color="rosybrown",linestyle="dashed")
plt.show()
    
    


