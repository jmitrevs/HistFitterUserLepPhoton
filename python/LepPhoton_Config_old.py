
################################################################
## In principle all you have to setup is defined in this file ##
################################################################

from configManager import configMgr
from ROOT import kBlack,kWhite,kGray,kRed,kPink,kMagenta,kViolet,kBlue,kAzure,kCyan,kTeal,kGreen,kSpring,kYellow,kOrange
from configWriter import TopLevelXML,Measurement,ChannelXML,Sample
from systematic import Systematic
import sys

## Read grid as argument:
analysisname = "LepPhoton"

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
#configMgr.cutsDict = {"SR":"1.0"}
configMgr.cutsDict["SREl"] = "1.0" #Only needed when doing directly the cuts (see tutorial)
configMgr.cutsDict["SRMu"] = "1.0" #Only needed when doing directly the cuts (see tutorial)
configMgr.cutsDict["WCREl"] = "1.0" #Only needed when doing directly the cuts (see tutorial)
configMgr.cutsDict["WCRMu"] = "1.0" #Only needed when doing directly the cuts (see tutorial)

# The systematics
ttbargammaNorm  = Systematic("ttbargammaNorm",configMgr.weights, 1.2, 0.8, "user","userOverallSys")
WgammaNorm  = Systematic("WgammaNorm",configMgr.weights, 1.16, 0.84, "user","userOverallSys")
WjetsNorm  = Systematic("WjetsNorm",configMgr.weights, 1.3, 0.7, "user","userOverallSys")
ZjetsNorm = Systematic("ZjetsNorm",configMgr.weights, 1.2, 0.8, "user","userOverallSys")
ZgammaNorm = Systematic("ZgammaNorm",configMgr.weights, 1.2, 0.8, "user","userOverallSys")
ttbarDilepNorm = Systematic("ttbarDilepNorm",configMgr.weights, 1.2, 0.8, "user","userOverallSys")
stNorm = Systematic("stNorm",configMgr.weights, 1.2, 0.8, "user","userOverallSys")
dibosonNorm = Systematic("dibosonNorm",configMgr.weights, 1.2, 0.8, "user","userOverallSys")
diphotonsNorm = Systematic("diphotonsNorm",configMgr.weights, 1.1, 0.9, "user","userOverallSys")
qcdElNorm = Systematic("qcdElNorm",configMgr.weights, 1.3, 0.7, "user","userOverallSys")
qcdMuNorm = Systematic("qcdMuNorm",configMgr.weights, 2.0, 0.0, "user","userOverallSys")

photon = Systematic("photon",configMgr.weights, 1.05, 0.95, "user","userOverallSys")
electron = Systematic("electron",configMgr.weights, 1.05, 0.95, "user","userOverallSys")
muon = Systematic("muon",configMgr.weights, 1.05, 0.95, "user","userOverallSys")
metMu = Systematic("metMu",configMgr.weights, 1.1, 0.9, "user","userOverallSys")
metEl = Systematic("metEl",configMgr.weights, 1.1, 0.9, "user","userOverallSys")

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

Ztautau = Sample("Ztautau",7) # cyan
Ztautau.setNormByTheory()
Ztautau.setStatConfig(True)
Ztautau.addSystematic(ZjetsNorm)

Wjets = Sample("Wjets",3) # green
Wjets.setStatConfig(True)


ttbarDilep = Sample("ttbarDilep",2) # red
ttbarDilep.setNormByTheory()
ttbarDilep.setStatConfig(True)
ttbarDilep.addSystematic(ttbarDilepNorm)

ttbarLepjets = Sample("ttbarLepjets",2) # red
ttbarLepjets.setStatConfig(True)

#if no CR
#Wjets.setNormByTheory()
#Wjets.addSystematic(WjetsNorm)
#ttbarLepjets.setNormByTheory()
#ttbarLepjets.addSystematic(ttbarDilepNorm)


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
st.setStatConfig(True)
#gj.setQCD()

data = Sample("data",kBlack)
data.setData()

commonSamples = [ttbargamma, Wgamma, Wjets, ttbarDilep, ttbarLepjets, st, Zgamma, Zleplep, Ztautau, diboson, gj, data]

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

#bkgOnly.addSystematic(photon)
 
meas = bkgOnly.addMeasurement(measName,measLumi,measLumiError)
meas.addPOI("mu_SIG")
#meas.addParamSetting("mu_Top","const",1.0)

SREl = bkgOnly.addChannel("cuts",["SREl"],cutsNBins,cutsBinLow,cutsBinHigh)
SRMu = bkgOnly.addChannel("cuts",["SRMu"],cutsNBins,cutsBinLow,cutsBinHigh)
WCREl = bkgOnly.addChannel("cuts",["WCREl"],cutsNBins,cutsBinLow,cutsBinHigh)
WCRMu = bkgOnly.addChannel("cuts",["WCRMu"],cutsNBins,cutsBinLow,cutsBinHigh)
bkgOnly.setBkgConstrainChannels([WCREl, WCRMu])

WCREl.getSample("Wjets").setNormFactor("mu_WjetsEl",1.,0.,5.)
SREl.getSample("Wjets").setNormFactor("mu_WjetsEl",1.,0.,5.)
WCRMu.getSample("Wjets").setNormFactor("mu_WjetsMu",1.,0.,5.)
SRMu.getSample("Wjets").setNormFactor("mu_WjetsMu",1.,0.,5.)
WCREl.getSample("ttbarLepjets").setNormFactor("mu_WjetsEl",1.,0.,5.)
SREl.getSample("ttbarLepjets").setNormFactor("mu_WjetsEl",1.,0.,5.)
WCRMu.getSample("ttbarLepjets").setNormFactor("mu_WjetsMu",1.,0.,5.)
SRMu.getSample("ttbarLepjets").setNormFactor("mu_WjetsMu",1.,0.,5.)
WCREl.getSample("gj").addSystematic(qcdElNorm)
SREl.getSample("gj").addSystematic(qcdElNorm)
WCRMu.getSample("gj").addSystematic(qcdMuNorm)
SRMu.getSample("gj").addSystematic(qcdMuNorm)

WCREl.addSample(diphotons)
SREl.addSample(diphotons)

## Discovery fit
#discovery = configMgr.addTopLevelXMLClone(bkgOnly,"SimpleChannel_Discovery")
#discovery.clearSystematics()
#sigSample = Sample("discoveryMode",kBlue)
#sigSample.setNormFactor("mu_SIG",0.5,0.,1.)
#sigSample.setNormByTheory()
#discovery.addSamples(sigSample)
#discovery.setSignalSample(sigSample)

#"SU_350_300_0_10","SU_500_450_0_10","SU_700_650_0_10","SU_800_750_0_10",,"SU_1000_950_0_10","SU_1150_1100_0_10","SU_1200_1150_0_10",
sigSamples = ["wino_1500_100", "wino_1500_150","wino_1500_200", "wino_1500_250", "wino_1500_300", "wino_600_500", "wino_700_600", "wino_800_600"]

for sig in sigSamples:
    myTopLvl = configMgr.addTopLevelXMLClone(bkgOnly,"SimpleChannel_%s"%sig) #This is cloning the fit such that the systematics are also considered for the signal
    sigSample = Sample(sig,kRed)
#    sigSample.setNormFactor("mu_SIG",1.,0.,500.)
#    sigSample.setNormFactor("mu_SIG",0.5,0.,1.)
    sigSample.setNormFactor("mu_SIG",1,0.,10.)
    sigSample.setStatConfig(True)

    # Decide whether to add theory systematics or not:
    sigSample.setNormByTheory()
    myTopLvl.addSamples(sigSample)
    myTopLvl.setSignalSample(sigSample)
    myTopLvl.setSignalChannels([SREl, SRMu])
