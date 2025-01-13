#Replication of the original code developed in Python through Julia implementation for more elegant and faster computation

using Plots
using PlotThemes
using LaTeXStrings
using QuantumOptics

b = SpinBasis(1//2)
δ2 = 0
ω = 1
g = 0.1
α = 0.1
Δ = 5*10^-3*ω

N = 13 #bosonic basis number
N = FockBasis(N) #bosonic basis

identity_v = tensor(identityoperator(N), identityoperator(N))
identity_d = tensor(identityoperator(b),identityoperator(b))

#Bosonic operators
B1 = tensor(identity_d, destroy(N), identityoperator(N))
B2 = tensor(identity_d, identityoperator(N), destroy(N))

H_V = ω*dagger(B1)*B1 + ω*dagger(B2)*B2

#fermions
N1 = tensor(sigmam(b)*sigmap(b), identityoperator(b), identity_v)
N2 = tensor(sigmap(b)*sigmam(b), identityoperator(b), identity_v)
N3 = tensor(identityoperator(b), sigmam(b)*sigmap(b), identity_v)
N4 = tensor(identityoperator(b), sigmap(b)*sigmam(b), identity_v)

#quantization of interaction
V_DV = g*(N1 + N3)*(dagger(B1) + B1) + g*(N2 + N4)*(dagger(B2) + B2) 

#total Hamiltonian

ϵ1(δ1) = eigenenergies(δ1/2*tensor(sigmaz(b), identityoperator(b), identity_v) + δ2/2*tensor(identityoperator(b),sigmaz(b), identity_v)
+ Δ*tensor(sigmax(b),identityoperator(b), identity_v) +  Δ*tensor(identityoperator(b), sigmax(b), identity_v) + H_V + V_DV,4, info=false)[1]


ϵ2(δ1) = eigenenergies((δ1/2*tensor(sigmaz(b), identityoperator(b), identity_v) + δ2/2*tensor(identityoperator(b),sigmaz(b), identity_v)
+ Δ*tensor(sigmax(b),identityoperator(b), identity_v) +  Δ*tensor(identityoperator(b), sigmax(b), identity_v) + H_V + V_DV),4, info=false)[2]

ϵ3(δ1) = eigenenergies((δ1/2*tensor(sigmaz(b), identityoperator(b), identity_v) + δ2/2*tensor(identityoperator(b),sigmaz(b), identity_v)
+ Δ*tensor(sigmax(b),identityoperator(b), identity_v) +  Δ*tensor(identityoperator(b), sigmax(b), identity_v) + H_V + V_DV),4,info=false)[3]

ϵ4(δ1) = eigenenergies((δ1/2*tensor(sigmaz(b), identityoperator(b), identity_v) + δ2/2*tensor(identityoperator(b),sigmaz(b), identity_v)
+ Δ*tensor(sigmax(b),identityoperator(b), identity_v) +  Δ*tensor(identityoperator(b), sigmax(b), identity_v) + H_V + V_DV),4, info=false)[4]


anticrossings = plot([ϵ1, ϵ2, ϵ3, ϵ4], -0.2, 0.2, title=L"m = l = 0"*" states",xlab=L"\delta_{1}",
ylab=L"E"*" (Units of "*L"\omega"*")", label=false)