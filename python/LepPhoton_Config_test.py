
################################################################
## In principle all you have to setup is defined in this file ##
################################################################

from configManager import configMgr
from ROOT import kBlack,kWhite,kGray,kRed,kPink,kMagenta,kViolet,kBlue,kAzure,kCyan,kTeal,kGreen,kSpring,kYellow,kOrange,TFile
from configWriter import TopLevelXML,Measurement,ChannelXML,Sample
from systematic import Systematic
import math
import sys

import metSyst
import phoScaleSyst

xsec = {}
    
def accSignalXsecs():
    # print "mgl, mC1, finalState, crossSection, Tot_error, K"
    f = TFile("output_gl_wino.root")
    ttree = f.Get("SignalUncertainties")
    for ev in ttree:
        key = "wino_%.0f_%.0f" % (ev.mgl, ev.mC1)
        if key in xsec:
            xsec[key][0] += ev.crossSection
            xsec[key][1] += (ev.crossSection*ev.Tot_error)**2
        else:
            xsec[key] = [ev.crossSection, (ev.crossSection*ev.Tot_error)**2]

    # for key, item in xsec.items():
    #     print "%s & %.3f & %.3f \\\\" % (key, item[0], math.sqrt(item[1])/item[0])

accSignalXsecs()

## Read grid as argument:
analysisname = "LepPhoton"

#old stuff
#mode='_AllUncertsXsecNominal'
#mode='_AllUncertsXsecMinus1Sigma'
#mode='_AllUncertsXsecPlus1Sigma'

mode='_NoTheoryUncertsXsecNominal'
#mode='_NoTheoryUncertsXsecMinus1Sigma'
#mode='_NoTheoryUncertsXsecPlus1Sigma'

analysisname += mode

## First define HistFactory attributes
configMgr.analysisName = analysisname

configMgr.outputFileName = "results/" + analysisname + "_AnalysisOutput.root"
   
## Scaling calculated by outputLumi / inputLumi
configMgr.inputLumi = 4.7  # Luminosity of input TTree after weighting
configMgr.outputLumi = 4.7 # Luminosity required for output histograms
configMgr.setLumiUnits("fb-1")

configMgr.blindSR = True

## setting the parameters of the hypothesis test
#configMgr.nTOYs=1000
configMgr.calculatorType=2 # 2=asymptotic calculator, 0=frequentist calculator
configMgr.testStatType=3 # 3=one-sided profile likelihood test statistic (LHC default)
configMgr.nPoints=20 # number of values scanned of signal-strength for upper-limit determination of signal strength.
#configMgr.doExclusion=True

## Set the files to read from #definitely for trees, but also for hists?)
#configMgr.inputFileNames = ["data/.root"]
#inputFileName = analysisname.rstrip()
#inputFileName = inputFileName.rstrip("NT")
#print "inputfilename = " + inputFileName

configMgr.inputFileNames = ["data/" + configMgr.analysisName + ".root"]
print "conf.inputFileNames = " + configMgr.inputFileNames[0]

## Suffix of nominal tree
configMgr.nomName = "_NoSys" #Actually not needed since I input directly histos

## Map regions to cut strings
configMgr.cutsDict["SREl"] = "1.0" #Only needed when doing directly the cuts (see tutorial)
configMgr.cutsDict["SRMu"] = "1.0" #Only needed when doing directly the cuts (see tutorial)

# The systematics
ttbargammaNorm  = Systematic("ttbargammaNorm",configMgr.weights, 1.40, 0.60, "user","userOverallSys")
WgammaNorm  = Systematic("WgammaNorm",configMgr.weights, 1.28, 0.72, "user","userOverallSys")
WjetsNormEl  = Systematic("WjetsNorm",configMgr.weights, 1.5, 0.5, "user","userOverallSys")
WjetsNormMu  = Systematic("WjetsNorm",configMgr.weights, 1.97, 0.03, "user","userOverallSys")
ZjetsNorm = Systematic("ZjetsNorm",configMgr.weights, 1.05, 0.95, "user","userOverallSys")
ZgammaNorm = Systematic("ZgammaNorm",configMgr.weights, 1.15, 0.85, "user","userOverallSys")
ttbarDilepNormEl = Systematic("ttbarDilepNorm",configMgr.weights, 1.136, 0.864, "user","userOverallSys")
ttbarDilepNormMu = Systematic("ttbarDilepNorm",configMgr.weights, 1.148, 0.852, "user","userOverallSys")
stNorm = Systematic("stNorm",configMgr.weights, 1.08, 0.92, "user","userOverallSys")
dibosonNorm = Systematic("dibosonNorm",configMgr.weights, 1.06, 0.94, "user","userOverallSys")
diphotonsNorm = Systematic("diphotonsNorm",configMgr.weights, 2.0, 0.5, "user","userOverallSys")
qcdElNorm = Systematic("qcdElNorm",configMgr.weights, 1.15, 0.85, "user","userOverallSys")

ttbarLepjetsNormEl = Systematic("ttbarLepjetsNorm",configMgr.weights, 4.0, 1.0-0.36, "user","userOverallSys")
ttbarLepjetsNormMu = Systematic("ttbarLepjetsNorm",configMgr.weights, 6.7, 1.0-0.33, "user","userOverallSys")

photon = Systematic("photon",configMgr.weights, 1.046, 0.954, "user","userOverallSys")
electron = Systematic("electron",configMgr.weights, 1.019, 0.981, "user","userOverallSys")
trigEl = Systematic("trigEl",configMgr.weights, 1.02, 0.98, "user","userOverallSys")
muon = Systematic("muon",configMgr.weights, 1.02, 0.98, "user","userOverallSys")
pileup = Systematic("pileup",configMgr.weights, 1.044, 0.956, "user","userOverallSys")

metElWgamma = Systematic("met",configMgr.weights, 1.280, 1-.212, "user","userOverallSys")
metElttgamma = Systematic("met",configMgr.weights, 1.139,1-.166, "user","userOverallSys")
metElttbarDilep = Systematic("met",configMgr.weights, 1.172, 1-.17, "user","userOverallSys")
metElWjets = Systematic("met",configMgr.weights, 1.372, 1-.192, "user","userOverallSys")
metElst = Systematic("met",configMgr.weights, 1.0, 1-.408, "user","userOverallSys")
metEldiboson = Systematic("met",configMgr.weights, 1.013, 1-.091, "user","userOverallSys")
metElZgamma = Systematic("met",configMgr.weights, 1.164, 1-.164, "user","userOverallSys")

metMuWgamma = Systematic("met",configMgr.weights, 1.132, 1-.098, "user","userOverallSys")
metMuttgamma = Systematic("met",configMgr.weights, 1.154,1-.099, "user","userOverallSys")
metMuttbarDilep = Systematic("met",configMgr.weights, 1.100, 1-.255, "user","userOverallSys")
metMuWjets = Systematic("met",configMgr.weights, 1.589, 1-.109, "user","userOverallSys")
metMust = Systematic("met",configMgr.weights, 1.235, 1-.327, "user","userOverallSys")
metMudiboson = Systematic("met",configMgr.weights, 1.046, 1-.04, "user","userOverallSys")
metMuZgamma = Systematic("met",configMgr.weights, 1.196, 1-.002, "user","userOverallSys")

metMuMuWgamma = Systematic("metMuMu",configMgr.weights, 1.027, 1-.027, "user","userOverallSys")
metMuMuttgamma = Systematic("metMuMu",configMgr.weights, 1.031, 1-.031, "user","userOverallSys")
metMuMuttbarDilep = Systematic("metMuMu",configMgr.weights, 1.025, 1-.025, "user","userOverallSys")
metMuMudiboson = Systematic("metMuMu",configMgr.weights, 1.032, 1-.032, "user","userOverallSys")
metMuMuZgamma = Systematic("metMuMu",configMgr.weights, 1.231, 1-.231, "user","userOverallSys")

# photon scale
phoScaleElWgamma = Systematic("phoScale",configMgr.weights, 1.018, 1-.018, "user","userOverallSys")
phoScaleElttgamma = Systematic("phoScale",configMgr.weights, 1.013,1-.013, "user","userOverallSys")
phoScaleElttbarDilep = Systematic("phoScale",configMgr.weights, 1.027, 1-.027, "user","userOverallSys")
phoScaleElst = Systematic("phoScale",configMgr.weights, 1.036, 1-.036, "user","userOverallSys")
phoScaleEldiboson = Systematic("phoScale",configMgr.weights, 1.029, 1-.029, "user","userOverallSys")
phoScaleElZgamma = Systematic("phoScale",configMgr.weights, 1.025, 1-.025, "user","userOverallSys")

phoScaleMuWgamma = Systematic("phoScale",configMgr.weights, 1.018, 1-.018, "user","userOverallSys")
phoScaleMuttgamma = Systematic("phoScale",configMgr.weights, 1.015,1-.015, "user","userOverallSys")
phoScaleMuttbarDilep = Systematic("phoScale",configMgr.weights, 1.028, 1-.028, "user","userOverallSys")
phoScaleMust = Systematic("phoScale",configMgr.weights, 1.023, 1-.023, "user","userOverallSys")
phoScaleMudiboson = Systematic("phoScale",configMgr.weights, 1.040, 1-.040, "user","userOverallSys")
phoScaleMuZgamma = Systematic("phoScale",configMgr.weights, 1.025, 1-.025, "user","userOverallSys")

## List of samples and their plotting colours. Associate dedicated systematics if applicable.

ttbargamma = Sample("ttbargamma",46) # brick
ttbargamma.setNormByTheory()
ttbargamma.setStatConfig(True)
ttbargamma.addSystematic(ttbargammaNorm)

Wgamma = Sample("Wgamma",7) # cyan
Wgamma.setNormByTheory()
Wgamma.setStatConfig(True)
Wgamma.addSystematic(WgammaNorm)

Zgamma = Sample("Zgamma",7) # cyan
Zgamma.setNormByTheory()
Zgamma.setStatConfig(True)
Zgamma.addSystematic(ZgammaNorm)

Zleplep = Sample("Zleplep",7) # cyan
Zleplep.setNormByTheory()
Zleplep.setStatConfig(True)
Zleplep.addSystematic(ZjetsNorm)

Wjets = Sample("Wjets",3) # green
Wjets.setNormByTheory(False)
Wjets.setStatConfig(True)
#Wjets.addSystematic(WjetsNorm)


ttbarDilep = Sample("ttbarDilep",2) # red
ttbarDilep.setNormByTheory()
ttbarDilep.setStatConfig(True)
#ttbarDilep.addSystematic(ttbarTtbarDilepNorm)

ttbarLepjets = Sample("ttbarLepjets",2) # red
ttbarLepjets.setStatConfig(True)
ttbarLepjets.setNormByTheory(False)
#ttbarLepjets.addSystematic(WjetsNorm)

diboson = Sample("diboson",8) # dark green
diboson.setNormByTheory()
diboson.setStatConfig(True)
diboson.addSystematic(dibosonNorm)

diphotons = Sample("diphotons",8) # dark green
diphotons.setNormByTheory()
diphotons.setStatConfig(True)
diphotons.addSystematic(diphotonsNorm)

st = Sample("st",8) # dark green
st.setNormByTheory()
st.setStatConfig(True)
st.addSystematic(stNorm)

gj = Sample("gj",28) # brown
gj.setStatConfig(True)
gj.addSystematic(qcdElNorm)
#gj.setQCD()

data = Sample("data",kBlack)
data.setData()

commonSamples = [ttbargamma, Wgamma, Wjets, ttbarDilep, ttbarLepjets, st, Zgamma, Zleplep, diboson, data]

## Parameters of the Measurement
measName = "BasicMeasurement"
measLumi = 1.
measLumiError = 0.039

## Parameters of Channels
cutsNBins = 1
cutsBinLow = 0.0
cutsBinHigh = 1.0

## Bkg-only fit (add the common systematics, which also affect the signal when cloning)
bkgOnly = configMgr.addTopLevelXML("LepPhoton_BkgOnly")
print '============',bkgOnly.name
bkgOnly.statErrThreshold=0.0#None #0.5
bkgOnly.addSamples(commonSamples)
 
meas = bkgOnly.addMeasurement(measName,measLumi,measLumiError)
meas.addPOI("mu_SIG")
#meas.addParamSetting("mu_Top","const",1.0)

SREl = bkgOnly.addChannel("cuts",["SREl"],cutsNBins,cutsBinLow,cutsBinHigh)
SRMu = bkgOnly.addChannel("cuts",["SRMu"],cutsNBins,cutsBinLow,cutsBinHigh)

bkgOnly.setSignalChannels([SREl, SRMu])

SREl.addSample(diphotons)

SREl.addSystematic(photon)
SREl.addSystematic(electron)
SREl.addSystematic(trigEl)
SREl.addSystematic(pileup)
SRMu.addSystematic(photon)
SRMu.addSystematic(muon)
SRMu.addSystematic(pileup)

SREl.getSample("Wjets").addSystematic(WjetsNormEl)
SRMu.getSample("Wjets").addSystematic(WjetsNormMu)
SREl.getSample("ttbarDilep").addSystematic(ttbarDilepNormEl)
SRMu.getSample("ttbarDilep").addSystematic(ttbarDilepNormMu)
SREl.getSample("ttbarLepjets").addSystematic(ttbarLepjetsNormEl)
SRMu.getSample("ttbarLepjets").addSystematic(ttbarLepjetsNormMu)

SREl.getSample("Wgamma").addSystematic(metElWgamma)
SREl.getSample("ttbargamma").addSystematic(metElttgamma)
SREl.getSample("ttbarDilep").addSystematic(metElttbarDilep)
SREl.getSample("Wjets").addSystematic(metElWjets)
SREl.getSample("st").addSystematic(metElst)
SREl.getSample("diboson").addSystematic(metEldiboson)
SREl.getSample("Zgamma").addSystematic(metElZgamma)

SRMu.getSample("Wgamma").addSystematic(metMuWgamma)
SRMu.getSample("ttbargamma").addSystematic(metMuttgamma)
SRMu.getSample("ttbarDilep").addSystematic(metMuttbarDilep)
SRMu.getSample("Wjets").addSystematic(metMuWjets)
SRMu.getSample("st").addSystematic(metMust)
SRMu.getSample("diboson").addSystematic(metMudiboson)
SRMu.getSample("Zgamma").addSystematic(metMuZgamma)

SRMu.getSample("Wgamma").addSystematic(metMuMuWgamma)
SRMu.getSample("ttbargamma").addSystematic(metMuMuttgamma)
SRMu.getSample("ttbarDilep").addSystematic(metMuMuttbarDilep)
SRMu.getSample("diboson").addSystematic(metMuMudiboson)
SRMu.getSample("Zgamma").addSystematic(metMuMuZgamma)

SREl.getSample("Wgamma").addSystematic(phoScaleElWgamma)
SREl.getSample("ttbargamma").addSystematic(phoScaleElttgamma)
SREl.getSample("ttbarDilep").addSystematic(phoScaleElttbarDilep)
SREl.getSample("st").addSystematic(phoScaleElst)
SREl.getSample("diboson").addSystematic(phoScaleEldiboson)
SREl.getSample("Zgamma").addSystematic(phoScaleElZgamma)

SRMu.getSample("Wgamma").addSystematic(phoScaleMuWgamma)
SRMu.getSample("ttbargamma").addSystematic(phoScaleMuttgamma)
SRMu.getSample("ttbarDilep").addSystematic(phoScaleMuttbarDilep)
SRMu.getSample("st").addSystematic(phoScaleMust)
SRMu.getSample("diboson").addSystematic(phoScaleMudiboson)
SRMu.getSample("Zgamma").addSystematic(phoScaleMuZgamma)

SREl.addSample(gj)
SREl.getSample("gj").removeSystematic("photon")
SREl.getSample("gj").removeSystematic("electron")
SREl.getSample("gj").removeSystematic("trigEl")
SREl.getSample("gj").removeSystematic("pileup")


## Discovery fit
#discovery = configMgr.addTopLevelXMLClone(bkgOnly,"SimpleChannel_Discovery")
#discovery.clearSystematics()
#sigSample = Sample("discoveryMode",kBlue)
#sigSample.setNormFactor("mu_SIG",0.5,0.,1.)
#sigSample.setNormByTheory()
#discovery.addSamples(sigSample)
#discovery.setSignalSample(sigSample)

#"SU_350_300_0_10","SU_500_450_0_10","SU_700_650_0_10","SU_800_750_0_10",,"SU_1000_950_0_10","SU_1150_1100_0_10","SU_1200_1150_0_10",
# sigSamples = ["wino_1500_100", "wino_1500_150", "wino_1500_200", "wino_1500_250", "wino_1500_300", "wino_1500_350",
#               "wino_1000_100", "wino_1000_150", "wino_1000_200", "wino_1000_250", "wino_1000_300", "wino_1000_350",
#               "wino_900_100", "wino_900_150", "wino_900_200", "wino_900_250", "wino_900_300", "wino_900_350",
#               "wino_800_100", "wino_800_150", "wino_800_200", "wino_800_250", "wino_800_300", "wino_800_350",
#               "wino_800_400", "wino_800_500", "wino_800_600", "wino_800_700", "wino_800_780",
#               "wino_700_100", "wino_700_150", "wino_700_200", "wino_700_250", "wino_700_300", "wino_700_350",
#               "wino_700_400", "wino_700_500", "wino_700_600", "wino_700_680",
#               "wino_600_100", "wino_600_200", "wino_600_300", "wino_600_400", "wino_600_500", "wino_600_580"]

sigSamples = ["wino_1500_200"]


for sig in sigSamples:
    myTopLvl = configMgr.addTopLevelXMLClone(bkgOnly,"SimpleChannel_%s"%sig) #This is cloning the fit such that the systematics are also considered for the signal
    sigSample = Sample(sig,kRed)
#    sigSample.setNormFactor("mu_SIG",1.,0.,500.)
#    sigSample.setNormFactor("mu_SIG",0.5,0.,1.)
    sigSample.setNormFactor("mu_SIG",1,0.,10.)
    sigSample.setStatConfig(True)
    sigXsecPair = xsec[sig]
    sigXsec = sigXsecPair[0]
    sigXsecUnc = math.sqrt(sigXsecPair[1])
    relUnc = sigXsecUnc / sigXsec
    theory = Systematic("theory",configMgr.weights, 1+relUnc, 1-relUnc, "user","userOverallSys")
    # if mode != '_NoTheoryUncertsXsecNominal':
    #     sigSample.addSystematic(theory)

    # Decide whether to add theory systematics or not:
    sigSample.setNormByTheory()
    myTopLvl.addSamples(sigSample)
    myTopLvl.setSignalSample(sigSample)
    myTopLvl.setSignalChannels([SREl, SRMu])

    # add met systematics
    metElVals = metSyst.metSystEl[sig]
    metMuVals = metSyst.metSystMu[sig]

    phoScaleVals = phoScaleSyst.phoScaleSyst[sig]

    metEl = Systematic("met",configMgr.weights, 1+metElVals[0], 1+metElVals[1], "user","userOverallSys")
    metMu = Systematic("met",configMgr.weights, 1+metMuVals[0], 1+metMuVals[1], "user","userOverallSys")
    metMuMu = Systematic("metMuMu",configMgr.weights, 1+metMuVals[2], 1-metMuVals[2], "user","userOverallSys")

    phoScaleEl = Systematic("phoScale",configMgr.weights, 1+phoScaleVals[0], 1-phoScaleVals[0], "user","userOverallSys")
    phoScaleMu = Systematic("phoScale",configMgr.weights, 1+phoScaleVals[1], 1-phoScaleVals[1], "user","userOverallSys")

    srel = myTopLvl.getChannel("cuts",["SREl"])
    srmu = myTopLvl.getChannel("cuts",["SRMu"])
    # srel.getSample(sig).addSystematic(metEl)
    # srmu.getSample(sig).addSystematic(metMu)
    # srmu.getSample(sig).addSystematic(metMuMu)
    # srel.getSample(sig).addSystematic(phoScaleEl)
    # srmu.getSample(sig).addSystematic(phoScaleMu)
    

