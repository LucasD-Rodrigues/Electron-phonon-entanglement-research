from qutip import *
import matplotlib.pyplot as plt
import numpy as np
from total_hamiltonian import *


#diagonalize matrix 
eigenvalues = np.array([(H(delta1)).eigenenergies() for delta1 in Delta_list])


plt.plot(Delta_list, eigenvalues[:,2],label="Eigenstate 1",color="rosybrown")
plt.plot(Delta_list, eigenvalues[:,1],label="Egenstate 2",color="black",linestyle="dashed")
plt.plot(Delta_list, eigenvalues[:,0],label="Eigenstate 3",color="black")
plt.plot(Delta_list, eigenvalues[:,3],label="Eigenstate 4",color="rosybrown",linestyle="dashed")
plt.show()