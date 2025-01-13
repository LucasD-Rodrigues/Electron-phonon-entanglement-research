using Plots
using PlotThemes
using LaTeXStrings

δ2 = 0
ω = 1
g = 0.1
α = 0.1

ϵ1(δ1) = 1/2*(δ1 + δ2) - 2*α^2*ω
ϵ2(δ1) = -1/2*(δ1 + δ2) - 2*α^2*ω
ϵ3(δ1) = 1/2*(δ1 + δ2)
ϵ4(δ1) = -1/2*(δ1 + δ2)

plot([ϵ1, ϵ2, ϵ3, ϵ4],-1, 1, title=L"m = l = 0"*" states",xlab=L"\delta_{1}",
ylab=L"E"*" (Units of "*L"\omega"*")", label=false)