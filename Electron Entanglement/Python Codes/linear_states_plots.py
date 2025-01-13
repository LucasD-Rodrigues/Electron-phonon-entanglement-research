from total_hamiltonian import *
from qutip import *
import matplotlib.pyplot as plt
import numpy as np

# define constants and variables
delta1= np.linspace(-1, 1, 200)

#write eigen energies function
epsilon_uup = 1/2*(delta1 + delta2) - 2*alpha**2*omega
epsilon_ddown = -1/2*(delta1 + delta2) - 2*alpha**2*omega
epsilon_udown = 1/2*(delta1 - delta2)
epsilon_dup = -1/2*(delta1 - delta2)

plt.plot(delta1,epsilon_ddown, color ='orange', linestyle ='dashed',
         linewidth = 1, label = "Eigenstate 1")
plt.plot(delta1,epsilon_uup, color ='red', linestyle ='dashed',
         linewidth = 1, label = "Eigenstate 2")
plt.plot(delta1,epsilon_dup,  color ='red',
         linewidth = 1, label = "Eigenstate 3")
plt.plot(delta1,epsilon_udown,  color ='orange',
         linewidth = 1, label="Eigenstate 4")
plt.legend(loc="upper left")

plt.title("Energy eingestates (No tunneling)")
plt.show()

