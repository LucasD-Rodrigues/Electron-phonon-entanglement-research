using Plots
using PlotThemes
using LaTeXStrings
using QuantumOptics

b = SpinBasis(1//2)
ω = 20*10^-3
δ2 = 0.1*ω
δ1 = δ2
g = 0.1*ω
α = g/ω
Δ = 5*10^-3*ω
Ω = 2*(Δ^2)/ω

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

H = δ1/2*tensor(identity_d,sigmaz,identity_v) + δ2/2*tensor(sigmaz,identity_d,identity_v) + Δ*tensor(identity_d,sigmax,identity_v) + Δ*tensor(sigmax,identity_d,identity_v) + H_V + V_DV

#initial state 
ψ0 = FockBasis(4,1)

θ = π*[0:1:1000;]
t_list = θ/Ω
x_axis = [0:1:1000]

ψₜ = timeevolution.schroedinger(t_list,ψ0,H)

ρ_red = [ptrace(ψ*dagger(ψ), 1) for ψ=ψₜ]
S = [entropy_vn(ρ)/log(2) for ρ=ρ_red]

plot(x_axis,S)

