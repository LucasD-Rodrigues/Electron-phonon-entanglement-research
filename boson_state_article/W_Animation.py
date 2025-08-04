##################################### Wigner Function Animations ########################################

from qutip import *
import numpy as np
from total_hamiltonian import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#simulation parameters
n = 1000
theta = np.pi*np.linspace(0,0.1,n)
times = theta/Omega0
x_axis = np.linspace(0,0.1,n)

psi0 = tensor(v10,v01,coherent(alpha=alpha, N=N), coherent(alpha=alpha,N=N))
#psi0 = Bell1
#psi0 = Bell2


#dynamics
__result__ = sesolve(H, psi0, times,options=Options(nsteps=50000, atol=1e-10, rtol=1e-8)) 
psi_t = __result__.states

# Prepare figure
xvec = np.linspace(-5, 5, 100)
fig, ax = plt.subplots()
X, Y = np.meshgrid(xvec, xvec)
w0 = wigner(ket2dm(psi0).ptrace(2), xvec, xvec)
im = ax.imshow(w0, extent=[xvec[0], xvec[-1], xvec[0], xvec[-1]], origin='lower', cmap='RdBu_r')
ax.set_title("Wigner Function Evolution")

#update animation frames
def update(n):
    w = wigner(psi_t[n].ptrace(2), xvec, xvec)
    im.set_array(w)
    ax.set_title(f"Wigner at $\\theta$ = {x_axis[n]:.4f} (units of $\pi$)")
    return [im]

#save file
anim = FuncAnimation(fig, update, frames=len(times), blit=True)
anim.save("wigner_animation.gif",writer="pillow", fps=10)
