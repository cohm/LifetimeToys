# collection of convenient functions to be used for relativistic kinematics calculations
import math, ROOT

def getLifetimeFunction(tauInNanoseconds, maxTimeInNanoseconds = 100):
    print("Will make a function for distribution of proper lifetimes for %f ns" % tauInNanoseconds)
    f = ROOT.TF1("ProperLifetimes_"+str(tauInNanoseconds).replace(".", "p"), "exp(-x/"+str(tauInNanoseconds)+"e-9)", 0, maxTimeInNanoseconds*1e-9)
    print(f)
    return f

def gammaFromBeta(beta):
    return 1/math.sqrt(1-beta**2)

def betaFromGamma(gamma):
    return math.sqrt(1-1/(gamma**2))

#for tau in [0.2, 4.04, 100.4]:
#    getLifetimeFunction(tau)
