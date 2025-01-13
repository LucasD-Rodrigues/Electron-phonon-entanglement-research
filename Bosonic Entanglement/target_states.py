from qutip import *
import numpy as np
from cts import *
import matplotlib.pyplot as plt

N = 13
cat = tensor(coherent(N,alpha),coherent(N,-alpha)) +  tensor(coherent(N,-alpha),coherent(N,alpha)) 
cat = cat.unit()
rho_cat = ket2dm(cat)

def W_target(rho):
    
    xvec = np.linspace(-5,5,200)
    W = wigner(rho.ptrace(0),xvec,xvec)
    X,Y = np.meshgrid(xvec,xvec)

    # contour plot
    plt.figure(figsize=(10,6))
    plt.subplot(111, aspect='equal')
    plt.contourf(X, Y, W, 200)
    plt.show()




