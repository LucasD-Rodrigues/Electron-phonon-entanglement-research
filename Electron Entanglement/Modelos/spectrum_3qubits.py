"""
Spyder Editor

Este é um arquivo de script temporário.
Diagonalização de uma matriz 8x8 - GHZ José
"""

import matplotlib.pyplot as plt
import numpy as np
from qutip import *

    #matrix values
J = 25.0
J12 = 1.0*J
J23= 1.0*J
#D1=J/8.0

#definição das energias tirando o detuning d1 (epsilon 1 no José)
#D1  =18.1/Vcou Programa original Augusto
#D2 = 46.7/Vcou Programa original Augusto
#EST = 56.7/Vcou Programa original Augusto 
#Matriz de 2 QBits do José
d1=0
d2=0
d3=0
E111 = d2+d3+J12+J23
E110 = d2-d3+J12-J23
E101 = d2+d3-J12-J23
E100 = -d2-d3-J12+J23
E011 = d2+d3-J12+J23
E010 = d2-d3-J12-J23
E001 = -d2+d3+J12-J23
E000 = -d2-d3+J12+J23
evals=[]
evecs=[]
evecg=[]
evals1=[]
evecs1=[]
dd = np.linspace(J/100,J,20) 
for D1 in dd: #np.arange(-3,3, 0.1):
  D2=D1
  D3=D1
  H3qb=[[E111+d1, D3, D2, 0, D1, 0, 0, 0], \
        [D3, E110+d1, 0, D2, 0, D1, 0, 0], \
        [D2, 0, E101+d1, D3, 0, 0, D1, 0], \
        [0, D2, D3, E100+d1, 0, 0, 0, D1], \
        [D1, 0, 0, 0, E011-d1, D3, D2, 0], \
        [0, D1, 0, 0, D3, E010-d1, 0, D2], \
        [0, 0, D2, 0, D2, 0, E001-d1, D3], \
        [0, 0, 0, D1, 0, D2, D3, E000-d1]]
  vals, vecs = np.linalg.eig(H3qb)
  evals.append(vals)
  evecs.append(vecs)
  QH3qb = Qobj(H3qb)
  vals1 = QH3qb.eigenenergies()
  vecs1 = QH3qb.eigenstates()
  evals1.append(vals1)
  evecs1.append(vecs1)
#Ordenando de menor a maior energia 
evals = np.sort(np.array(evals))
evecs = np.sort(np.array(evecs))
print('evals subrutina Augusto',evals)
print('evals1 qutip',evals1)

for i in range(8):
    print(np.dot(evecs[i,0],evecs[i,0]))

# print('COMPARANDO')    
# print(np.dot(evecs[0,1],evecs[0,1]))
# print(np.dot(evecs[0,2],evecs[0,2]))
# print(np.dot(evecs[0,3],evecs[0,3]))
# print(np.dot(evecs[0,4],evecs[0,4]))
# print(np.dot(evecs[0,5],evecs[0,5]))
# print(np.dot(evecs[0,6],evecs[0,6]))
# print(np.dot(evecs[0,7],evecs[0,7]))
   

#Operações com os autoestados
# c00= (evecs[:,0,0])**2
# c01= (evecs[:,0,1])**2
# c02= (evecs[:,0,2])**2 

# c10= (evecs[:,1,0])**2
# c11= (evecs[:,1,1])**2
# c12= (evecs[:,1,2])**2

# c20= (evecs[:,2,0])**2
# c21= (evecs[:,2,1])**2
# c22= (evecs[:,2,2])**2
# for i in range(7):

#gráficos
#Espectro
plt.plot(dd, evals[:,0], 'r:o')
plt.plot(dd, evals[:,1], 'r--')
plt.plot(dd, evals[:,2],'b:')
plt.plot(dd, evals[:,3],'b*')
plt.plot(dd, evals[:,4],'b-.')
plt.plot(dd, evals[:,5],'b+')
plt.plot(dd, evals[:,6],'ko')
plt.plot(dd, evals[:,7],'k-')
plt.show()

#So GHZ
#plt.plot(dd, evals[:,6],'k-o')
#plt.plot(dd, evals[:,7],'r--*')
#plt.show()

#So FLIP
# plt.plot(dd, evals[:,0], 'k-')
# plt.plot(dd, evals[:,1], 'r--')
# plt.show()

#Diferenças de energias
#plt.plot(dd, np.abs(evals[:,6]-evals[:,7]-(dd*dd*dd/(J*J))),'r--')
#plt.plot(dd, np.abs(evals[:,0]-evals[:,1]-(dd*dd*dd/(J*J))),'k+')
#plt.show()
