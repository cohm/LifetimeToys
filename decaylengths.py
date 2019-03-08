# simple script for studying lab-frame decay lengths for LLPs

import math
import ROOT
import AtlasStyle
import kinematics as kin

tau = 1e-9
c = 3e8

ROOT.gStyle.SetPadRightMargin(0.15)

cGamma = ROOT.TCanvas("DecayLengthVsGamma", "DecayLengthVsGamma")
# we have exponential lifetimes, what does that do to the distribution of decay points
# as function of gamma? let's get a lifetime function, draw random taus and scale by gamma
# and multiply by beta*c
fLifetimeGenerator = kin.getLifetimeFunction(1)
h2 = ROOT.TH2F("DecayLengthVsGammaHisto", "#Delta t * #gamma * #beta * c;#gamma;Decay length [m]", 50, 1, 6, 100, 0, 5)
for gamma in [x / 99.9999 for x in range(100, 600, 2)]:
    #print("Will now generate decay positions for gamma = %f" % gamma)
    for e in range(100000):
        h2.Fill(gamma, fLifetimeGenerator.GetRandom()*gamma*kin.betaFromGamma(gamma)*c)
h2.SetContour(99)
h2.Draw("COLZ")
p = h2.ProfileX("proj", 1, -1, "s")
p.Draw("SAME")
cGamma.SetLogz(1)
cGamma.Print("DecayLengthVsGamma.pdf")


# create a function which calculates the decay length for a 1 ns particle as a function of gamma
# deltat*gamma*beta*c
fDecayGamma = ROOT.TF1("fGamma", "%E*x*sqrt(1-1/(x*x))*%E" % (tau, c), 1, 6)
fDecayGamma.SetTitle("#Deltat*#gamma*#beta*c;#gamma;Decay length [m]")
fDecayGamma.SetLineColor(ROOT.kGreen+3)
fDecayGamma.Draw("SAME")
# and a function which just uses c*tau
#f2 = ROOT.TF2("f2", "1e-9*3e8+0.0000001*x", 1, 5)
fctau = ROOT.TLine(1, c*tau, 6, c*tau)
fctau.SetLineColor(2)
fctau.SetLineWidth(2)
fctau.Draw()
cGamma.Print("DecayLengthVsGamma_wFunctions.pdf")

leg = ROOT.TLegend(0.62, 0.71, 0.82, 0.91)
leg.AddEntry(fDecayGamma, "#font[52]{#Deltat*#gamma*#beta*c}", "l")
leg.AddEntry(fctau, "#font[52]{c#tau}", "l")
leg.SetBorderSize(0)
leg.SetFillStyle(0)
leg.Draw()

# add points for interesting relevant cases, e.g. a very heavy gluino and a light scalar from Higgs with typical momenta
g = ROOT.TGraph(2)
gluino = ROOT.TLorentzVector()
gluino.SetPtEtaPhiM(1000, 0, 0, 2500)
g.SetPoint(0, gluino.Gamma(), fDecayGamma.Eval(gluino.Gamma()))
lightScalar = ROOT.TLorentzVector()
lightScalar.SetPtEtaPhiM(50, 0, 0, 10)
g.SetPoint(1, lightScalar.Gamma(), fDecayGamma.Eval(lightScalar.Gamma()))
g.SetMarkerStyle(29)
g.SetMarkerSize(2.0)
g.SetMarkerColor(ROOT.kRed)
g.Draw("P")
cGamma.Print("DecayLengthVsGamma_wFunctions_wPoints.pdf")

# and as function of beta
#cBeta = ROOT.TCanvas("DecayLengthVsBeta", "DecayLengthVsBeta")
# deltat*gamma*beta*c
#fDecayGamma = ROOT.TF1("fBeta", "%E*(1/sqrt(1-x*x))*x*%E" % (tau, c), 0, 1)
#fDecayGamma.SetTitle("#Delta t * #gamma * #beta * c;#beta;Decay length [m]")
#fDecayGamma.SetLineColor(ROOT.kGreen+3)
#fDecayGamma.Draw()
## and a function which just uses c*tau
##f2 = ROOT.TF2("f2", "1e-9*3e8+0.0000001*x", 1, 5)
#fctau2 = ROOT.TLine(0, c*tau, 1, c*tau)
#fctau2.SetLineColor(2)
#fctau2.Draw()
