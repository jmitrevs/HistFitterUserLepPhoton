
################################################################
## In principle all you have to setup is defined in this file ##
################################################################

from configManager import configMgr
from ROOT import kBlack,kWhite,kGray,kRed,kPink,kMagenta,kViolet,kBlue,kAzure,kCyan,kTeal,kGreen,kSpring,kYellow,kOrange,TFile
from configWriter import Sample
from systematic import Systematic
import math
import sys

#import Tables

from InputYields import *
winoyields = Yields("python/signal.txt", True)
# winoyields = Yields("python/signal_test.txt", True)
backyields = Yields("python/backyields.txt", True)

#old stuff
#mode='_AllUncertsXsecNominal'
#mode='_AllUncertsXsecMinus1Sigma'
#mode='_AllUncertsXsecPlus1Sigma'

mode='_NoTheoryUncertsXsecNominal'
#mode='_NoTheoryUncertsXsecMinus1Sigma'
#mode='_NoTheoryUncertsXsecPlus1Sigma'

ELECTRON = 0
MUON = 1
BOTH = 2

#leptons = BOTH
leptons = ELECTRON
#leptons = MUON

#xsec = {}
    
# def accSignalXsecs():
#     # print "mgl, mC1, finalState, crossSection, Tot_error, K"
#     f = TFile("output_gl_wino.root")
#     ttree = f.Get("SignalUncertainties")
#     for ev in ttree:
#         key = "wino_%.0f_%.0f" % (ev.mgl, ev.mC1)
#         if key in xsec:
#             xsec[key][0] += ev.crossSection
#             xsec[key][1] += (ev.crossSection*ev.Tot_error)**2
#         else:
#             xsec[key] = [ev.crossSection, (ev.crossSection*ev.Tot_error)**2]

#     # for key, item in xsec.items():
#     #     print "%s & %.3f & %.3f \\\\" % (key, item[0], math.sqrt(item[1])/item[0])

# accSignalXsecs()

theoryUnc = {
    "wino_100" : 0.0761,
    "wino_150" : 0.0663,
    "wino_200" : 0.0640,
    "wino_250" : 0.0661,
    "wino_300" : 0.0687,
    "wino_350" : 0.0704,
    "wino_400" : 0.0757,
    "wino_450" : 0.0787,
    "wino_500" : 0.0811
}

WgammaScale = {
    "SRW" : 0.064,
    "HMThHT" : 0.189,
    "HMEThHT" : 0.010
}

ttbargammaScale = {
    "SRW" : 0.061,
    "WCRhHT" : 0.051,
    "HMThHT" : 0.097,
    "HMEThHT" : 0.033
}

WjetsScale = {
    "SRW" : 0.132,
    "HMThHT" : 0.101,
    "HMEThHT" : 0.101
}

WgammaPDF = {
    "SRW" : (-0.038, 0.034),
    "HMThHT" : (-0.015, 0.015),
    "HMEThHT" : (-0.013, 0.019)
}

ttbargammaPDF = {
    "SRW" : 0.061,
    "WCRhHT" : 0.051,
    "HMThHT" : 0.097,
    "HMEThHT" : 0.033
}

WjetsPDF = {
    "SRW" : 0.018,
    "HMThHT" : 0.016,
    "HMEThHT" : 0.015
}

## Read grid as argument:
analysisname = "LepPhoton8TeV_weak"

analysisname += mode
if leptons == ELECTRON:
    analysisname += "_electron"
elif leptons == MUON:
    analysisname += "_muon"
elif leptons == BOTH:
    pass
else:
    print "leptons incorrectly assigned to:", leptons
    exit(1)

## First define HistFactory attributes
configMgr.analysisName = analysisname

configMgr.outputFileName = "results/" + analysisname + "_AnalysisOutput.root"
   
## Scaling calculated by outputLumi / inputLumi
configMgr.inputLumi = 20.3  # Luminosity of input TTree after weighting
configMgr.outputLumi = 20.3 # Luminosity required for output histograms
configMgr.setLumiUnits("fb-1")

configMgr.blindSR = False

## setting the parameters of the hypothesis test
configMgr.doExclusion=True
#configMgr.nTOYs=1000
configMgr.calculatorType=2 # 2=asymptotic calculator, 0=frequentist calculator
configMgr.testStatType=3 # 3=one-sided profile likelihood test statistic (LHC default)
configMgr.nPoints=20 # number of values scanned of signal-strength for upper-limit determination of signal strength.

## Set the files to read from #definitely for trees, but also for hists?)
#configMgr.inputFileNames = ["data/.root"]
#inputFileName = analysisname.rstrip()
#inputFileName = inputFileName.rstrip("NT")
#print "inputfilename = " + inputFileName

#configMgr.inputFileNames = ["data/" + configMgr.analysisName + ".root"]
#print "conf.inputFileNames = " + configMgr.inputFileNames[0]

## Suffix of nominal tree
configMgr.nomName = "_NoSys" #Actually not needed since I input directly histos

## Map regions to cut strings
configMgr.cutsDict["SRWEl"] = "1.0" #Only needed when doing directly the cuts (see tutorial)
configMgr.cutsDict["SRWMu"] = "1.0" #Only needed when doing directly the cuts (see tutorial)
configMgr.cutsDict["WCRhHT"] = "1.0" #Only needed when doing directly the cuts (see tutorial)
configMgr.cutsDict["HMEThHTEl"] = "1.0" #Only needed when doing directly the cuts (see tutorial)
configMgr.cutsDict["HMEThHTMu"] = "1.0" #Only needed when doing directly the cuts (see tutorial)
configMgr.cutsDict["HMThHTEl"] = "1.0" #Only needed when doing directly the cuts (see tutorial)
configMgr.cutsDict["HMThHTMu"] = "1.0" #Only needed when doing directly the cuts (see tutorial)

# The systematics
ttbargammaNorm  = Systematic("ttbargammaNorm",configMgr.weights, 1.40, 0.60, "user","userOverallSys")
#WgammaNorm  = Systematic("WgammaNorm",configMgr.weights, 1.40, 0.60, "user","userOverallSys")
#WjetsNormEl  = Systematic("WjetsNorm",configMgr.weights, 1.5, 0.5, "user","userOverallSys")
#WjetsNormMu  = Systematic("WjetsNorm",configMgr.weights, 1.97, 0.03, "user","userOverallSys")
ZjetsNorm = Systematic("ZjetsNorm",configMgr.weights, 1.5, 0.5, "user","userOverallSys")
ZgammaNorm = Systematic("ZgammaNorm",configMgr.weights, 1.5, 0.5, "user","userOverallSys")
ttbarDilepNorm = Systematic("ttbarDilepNorm",configMgr.weights, 1.06, 1-0.06, "user","userOverallSys")
singletopNorm = Systematic("singletopNorm",configMgr.weights, 1.5, 0.5, "user","userOverallSys")
dibosonNorm = Systematic("dibosonNorm",configMgr.weights, 1.5, 0.5, "user","userOverallSys")
diphotonsNorm = Systematic("diphotonsNorm",configMgr.weights, 2.0, 0.5, "user","userOverallSys")
#qcdElNorm = Systematic("qcdElNorm",configMgr.weights, 1.15, 0.85, "user","userOverallSys")
#qcdMuNorm = Systematic("qcdMuNorm",configMgr.weights, 1.15, 0.85, "user","userOverallSys")

photon = Systematic("photon",configMgr.weights, 1.011, 1-0.011, "user","userOverallSys")
electron = Systematic("electron",configMgr.weights, 1.01, 0.99, "user","userOverallSys")
trig = Systematic("trig",configMgr.weights, 1.0001, 1-0.0158, "user","userOverallSys")
muon = Systematic("muon",configMgr.weights, 1.004, 0.996, "user","userOverallSys")
elToPhoton = Systematic("elToPhoton",configMgr.weights, 1.07, 1-0.07, "user","userOverallSys")

## List of samples and their plotting colours. Associate dedicated systematics if applicable.

ttbargamma = Sample("ttbargamma",46) # brick
ttbargamma.setNormByTheory()
ttbargamma.setStatConfig(True)
ttbargamma.addSystematic(ttbargammaNorm)

Wgamma = Sample("Wgamma",7) # cyan
Wgamma.setNormFactor("mu_Wgamma",1.0,0.,5.)
#Wgamma.setNormRegions([("WCRhHT", "cuts")])
Wgamma.setStatConfig(True)
#Wgamma.addSystematic(WgammaNorm)

Zgamma = Sample("Zgamma",kViolet) # cyan
Zgamma.setNormByTheory()
Zgamma.setStatConfig(True)
Zgamma.addSystematic(ZgammaNorm)

Zjets = Sample("Zjets",kBlue) # cyan
Zjets.setNormByTheory()
Zjets.setStatConfig(True)
Zjets.addSystematic(ZjetsNorm)

Wjets = Sample("Wjets",3) # green
Wjets.setNormByTheory(False)
Wjets.setStatConfig(True)
#Wjets.addSystematic(WjetsNorm)


ttbarDilep = Sample("ttbarDilep",2) # red
ttbarDilep.setNormByTheory()
ttbarDilep.setStatConfig(True)
ttbarDilep.addSystematic(ttbarDilepNorm)

#ttbarLepjets = Sample("ttbarLepjets",2) # red
#ttbarLepjets.setStatConfig(True)
#ttbarLepjets.setNormByTheory(False)
#ttbarLepjets.addSystematic(WjetsNorm)

diboson = Sample("diboson",kGreen+4) # dark green
diboson.setNormByTheory()
diboson.setStatConfig(True)
diboson.addSystematic(dibosonNorm)

diphotons = Sample("diphotons",kYellow-1) # dark green
diphotons.setNormByTheory()
diphotons.setStatConfig(True)
diphotons.addSystematic(diphotonsNorm)

singletop = Sample("singletop",kOrange) # dark green
singletop.setNormByTheory()
singletop.setStatConfig(True)
singletop.addSystematic(singletopNorm)

gammajets = Sample("gammajets",28) # brown
gammajets.setStatConfig(True)
gammajets.setNormByTheory(False)
#gammajets.addSystematic(qcdElNorm)
#gammajets.setQCD()

data = Sample("data",kBlack)
data.setData()


commonSamples = [ttbargamma, Wgamma, Wjets, ttbarDilep, singletop, Zgamma, Zjets, diboson, gammajets, data]

for lepton in ('El', 'Mu'):
    for region in ("WCRhHT", "HMEThHT", "HMThHT", "SRW"):
        regionName = region+lepton
        if regionName == 'WCRhHTEl':
            regionName = 'WCRhHT'
        elif regionName == 'WCRhHTMu':
            continue
        ttbargamma.buildHisto([backyields.GetYield(lepton, region, "ttbargamma")], regionName, "cuts")
        ttbargamma.buildStatErrors([backyields.GetYieldUnc(lepton, region, "ttbargamma")], regionName, "cuts")
        Wgamma.buildHisto([backyields.GetYield(lepton, region, "Wgamma")], regionName, "cuts")
        Wgamma.buildStatErrors([backyields.GetYieldUnc(lepton, region, "Wgamma")], regionName, "cuts")
        Wjets.buildHisto([backyields.GetYield(lepton, region, "Wjets")], regionName, "cuts")
        Wjets.buildStatErrors([backyields.GetYieldUnc(lepton, region, "Wjets")], regionName, "cuts")
        ttbarDilep.buildHisto([backyields.GetYield(lepton, region, "ttbarDilep")], regionName, "cuts")
        ttbarDilep.buildStatErrors([backyields.GetYieldUnc(lepton, region, "ttbarDilep")], regionName, "cuts")
        singletop.buildHisto([backyields.GetYield(lepton, region, "singletop")], regionName, "cuts")
        singletop.buildStatErrors([backyields.GetYieldUnc(lepton, region, "singletop")], regionName, "cuts")
        Zgamma.buildHisto([backyields.GetYield(lepton, region, "Zgamma")], regionName, "cuts")
        Zgamma.buildStatErrors([backyields.GetYieldUnc(lepton, region, "Zgamma")], regionName, "cuts")
        Zjets.buildHisto([backyields.GetYield(lepton, region, "Zjets")], regionName, "cuts")
        Zjets.buildStatErrors([backyields.GetYieldUnc(lepton, region, "Zjets")], regionName, "cuts")
        diboson.buildHisto([backyields.GetYield(lepton, region, "diboson")], regionName, "cuts")
        diboson.buildStatErrors([backyields.GetYieldUnc(lepton, region, "diboson")], regionName, "cuts")
        gammajets.buildHisto([backyields.GetYield(lepton, region, "gammajets")], regionName, "cuts")
        gammajets.buildStatErrors([backyields.GetYieldUnc(lepton, region, "gammajets")], regionName, "cuts")
        data.buildHisto([backyields.GetYield(lepton, region, "data")], regionName, "cuts")
        data.buildStatErrors([backyields.GetYieldUnc(lepton, region, "data")], regionName, "cuts")
        if lepton == 'El':
            diphotons.buildHisto([backyields.GetYield(lepton, region, "diphotons")], regionName, "cuts")
            diphotons.buildStatErrors([backyields.GetYieldUnc(lepton, region, "diphotons")], regionName, "cuts")



## Parameters of the Measurement
measName = "BasicMeasurement"
measLumi = 1.
measLumiError = 0.028

## Parameters of Channels
cutsNBins = 1
cutsBinLow = 0.5
cutsBinHigh = 1.5

## Bkg-only fit (add the common systematics, which also affect the signal when cloning)
bkgOnly = configMgr.addTopLevelXML("LepPhoton8TeV_BkgOnly")
print '============',bkgOnly.name
bkgOnly.statErrThreshold=0.0#None #0.5
bkgOnly.addSamples(commonSamples)
 
meas = bkgOnly.addMeasurement(measName,measLumi,measLumiError)
meas.addPOI("mu_SIG")
#meas.addParamSetting("mu_Top","const",1.0)


WCRhHT = bkgOnly.addChannel("cuts",["WCRhHT"],cutsNBins,cutsBinLow,cutsBinHigh)
bkgOnly.setBkgConstrainChannels([WCRhHT])

elChannels = [WCRhHT]           # by convention
muChannels = []

if myFitType != FitType.Background:
    if leptons == BOTH:
        print "setting both channels"
        SRWEl = bkgOnly.addChannel("cuts",["SRWEl"],cutsNBins,cutsBinLow,cutsBinHigh)
        SRWMu = bkgOnly.addChannel("cuts",["SRWMu"],cutsNBins,cutsBinLow,cutsBinHigh)
        bkgOnly.setSignalChannels([SRWEl, SRWMu])
        elChannels.append(SRWEl)
        muChannels.append(SRWMu)
    elif leptons == ELECTRON:
        print "setting only electron"
        SRWEl = bkgOnly.addChannel("cuts",["SRWEl"],cutsNBins,cutsBinLow,cutsBinHigh)
        bkgOnly.setSignalChannels([SRWEl])
        elChannels.append(SRWEl)
    else:
        print "setting only muons"
        SRWMu = bkgOnly.addChannel("cuts",["SRWMu"],cutsNBins,cutsBinLow,cutsBinHigh)
        bkgOnly.setSignalChannels([SRWMu])
        muChannels.append(SRWMu)


if myFitType == FitType.Background:

    print "In Background"

    HMEThHTEl = bkgOnly.addChannel("cuts",["HMEThHTEl"],cutsNBins,cutsBinLow,cutsBinHigh)
    HMEThHTMu = bkgOnly.addChannel("cuts",["HMEThHTMu"],cutsNBins,cutsBinLow,cutsBinHigh)
    HMThHTEl = bkgOnly.addChannel("cuts",["HMThHTEl"],cutsNBins,cutsBinLow,cutsBinHigh)
    HMThHTMu = bkgOnly.addChannel("cuts",["HMThHTMu"],cutsNBins,cutsBinLow,cutsBinHigh)

    elChannels.append(HMEThHTEl)
    elChannels.append(HMThHTEl)
    muChannels.append(HMEThHTMu)
    muChannels.append(HMThHTMu)

    SRWEl = bkgOnly.addChannel("cuts",["SRWEl"],cutsNBins,cutsBinLow,cutsBinHigh)
    SRWMu = bkgOnly.addChannel("cuts",["SRWMu"],cutsNBins,cutsBinLow,cutsBinHigh)
    elChannels.append(SRWEl)
    muChannels.append(SRWMu)

    bkgOnly.setValidationChannels([ 
            HMEThHTEl, HMEThHTMu, 
            HMThHTEl, HMThHTMu,
            SRWEl, SRWMu
            ])


for elRegion in elChannels:
    elRegion.addSample(diphotons)
    elRegion.addSystematic(electron)

    elRegion.getSample("gammajets").removeSystematic("electron")

    if elRegion == WCRhHT:
        elRegion.addSystematic(muon)
        elRegion.getSample("gammajets").removeSystematic("muon")
        #elRegion.getSample("Wjets").removeSystematic("muon")
        #elRegion.getSample("Wjets").removeSystematic("electron")

for muRegion in muChannels:
    muRegion.addSystematic(muon)

    muRegion.getSample("gammajets").removeSystematic("muon")

for sample in commonSamples:
    print "sampleName",sample.name

for region in elChannels + muChannels:
    region.addSystematic(photon)
    region.addSystematic(trig)
    region.getSample("gammajets").removeSystematic("photon")
    region.getSample("gammajets").removeSystematic("trig")

    region.getSample("ttbarDilep").addSystematic(elToPhoton)
    region.getSample("diboson").addSystematic(elToPhoton)
    region.getSample("singletop").addSystematic(elToPhoton)

    #region.getSample("Wjets").removeSystematic("photon")
    #region.getSample("Wjets").removeSystematic("trig")

    regionName = region.name[5:-2]
    lepton = region.name[-2:]
    if lepton == 'HT':
        lepton = 'El'
        regionName = region.name[5:]

    # scale and pdf
    if regionName != 'WCRhHT':
        region.getSample("Wgamma").addSystematic(Systematic("WgammaScale",
                                                          configMgr.weights, 
                                                          1+WgammaScale[regionName],
                                                          1-WgammaScale[regionName], 
                                                          "user","userOverallSys"))
        region.getSample("Wgamma").addSystematic(Systematic("WgammaPDF",
                                                          configMgr.weights, 
                                                          1+WgammaPDF[regionName][1],
                                                          1+WgammaPDF[regionName][0], 
                                                          "user","userOverallSys"))

        region.getSample("Wjets").addSystematic(Systematic("WjetsScale",
                                                          configMgr.weights, 
                                                          1+WjetsScale[regionName],
                                                          1-WjetsScale[regionName], 
                                                          "user","userOverallSys"))
        region.getSample("Wjets").addSystematic(Systematic("WjetsPDF",
                                                          configMgr.weights, 
                                                          1+WjetsPDF[regionName],
                                                          1-WjetsPDF[regionName], 
                                                          "user","userOverallSys"))

    region.getSample("ttbargamma").addSystematic(Systematic("ttbargammaScale",
                                                            configMgr.weights, 
                                                            1+ttbargammaScale[regionName],
                                                            1-ttbargammaScale[regionName], 
                                                            "user","userOverallSys"))
    region.getSample("ttbargamma").addSystematic(Systematic("ttbargammaPDF",
                                                            configMgr.weights, 
                                                            1+ttbargammaPDF[regionName],
                                                            1-ttbargammaPDF[regionName], 
                                                            "user","userOverallSys"))
        
    for sample in ['ttbargamma', 'Wgamma', 'Wjets', 'ttbarDilep', 'singletop', 'Zgamma', 'Zjets', 'diboson']:
        if sample == 'Wjets' and regionName == 'WCRhHT':
            continue
        region.getSample(sample).addSystematic(Systematic("pileup",
                                                          configMgr.weights, 
                                                          1+backyields.GetPileUp(lepton, regionName, sample), 
                                                          1+backyields.GetPileDown(lepton, regionName, sample), 
                                                          "user","userOverallSys"))

        region.getSample(sample).addSystematic(Systematic("jes",
                                                          configMgr.weights, 
                                                          1+backyields.GetJESUp(lepton, regionName, sample), 
                                                          1+backyields.GetJESDown(lepton, regionName, sample), 
                                                          "user","userOverallSys"))

        region.getSample(sample).addSystematic(Systematic("jer",
                                                          configMgr.weights, 
                                                          1+backyields.GetJER(lepton, regionName, sample), 
                                                          1-backyields.GetJER(lepton, regionName, sample), 
                                                          "user","userOverallSys"))

        region.getSample(sample).addSystematic(Systematic("muonScale",
                                                          configMgr.weights, 
                                                          1+backyields.GetMuonScaleUp(lepton, regionName, sample), 
                                                          1+backyields.GetMuonScaleDown(lepton, regionName, sample), 
                                                          "user","userOverallSys"))

        region.getSample(sample).addSystematic(Systematic("muonMSRes",
                                                          configMgr.weights, 
                                                          1+backyields.GetMuonMSRes(lepton, regionName, sample)/2.0, 
                                                          1-backyields.GetMuonMSRes(lepton, regionName, sample)/2.0, 
                                                          "user","userOverallSys"))

        region.getSample(sample).addSystematic(Systematic("muonIDRes",
                                                          configMgr.weights, 
                                                          1+backyields.GetMuonIDRes(lepton, regionName, sample)/2.0, 
                                                          1-backyields.GetMuonIDRes(lepton, regionName, sample)/2.0, 
                                                          "user","userOverallSys"))

        region.getSample(sample).addSystematic(Systematic("egScale",
                                                          configMgr.weights, 
                                                          1+backyields.GetEgScaleUp(lepton, regionName, sample), 
                                                          1+backyields.GetEgScaleDown(lepton, regionName, sample), 
                                                          "user","userOverallSys"))

        region.getSample(sample).addSystematic(Systematic("egPS",
                                                          configMgr.weights, 
                                                          1+backyields.GetEgPSUp(lepton, regionName, sample), 
                                                          1+backyields.GetEgPSDown(lepton, regionName, sample), 
                                                          "user","userOverallSys"))

        region.getSample(sample).addSystematic(Systematic("egMaterial",
                                                          configMgr.weights, 
                                                          1+backyields.GetEgMatUp(lepton, regionName, sample), 
                                                          1+backyields.GetEgMatDown(lepton, regionName, sample), 
                                                          "user","userOverallSys"))

        region.getSample(sample).addSystematic(Systematic("egRes",
                                                          configMgr.weights, 
                                                          1+backyields.GetEgResUp(lepton, regionName, sample), 
                                                          1+backyields.GetEgResDown(lepton, regionName, sample), 
                                                          "user","userOverallSys"))

    region.getSample("Wjets").addSystematic(Systematic("WjetsNorm"+lepton,
                                                       configMgr.weights, 
                                                       1+backyields.GetTransFact(lepton, regionName, "Wjets"), 
                                                       1-backyields.GetTransFact(lepton, regionName, "Wjets"), 
                                                       "user","userOverallSys"))

    

    region.getSample("gammajets").addSystematic(Systematic("mat"+lepton,
                                                      configMgr.weights, 
                                                      1+backyields.GetMatrixUp(lepton, regionName, "gammajets"), 
                                                      1+backyields.GetMatrixDown(lepton, regionName, "gammajets"), 
                                                      "user","userOverallSys"))


    if regionName == 'WCRhHT':
        # also add the muon versions
        region.getSample("Wjets").addSystematic(Systematic("WjetsNormMu",
                                                           configMgr.weights, 
                                                           1+backyields.GetTransFactAlt(lepton, regionName, "Wjets"), 
                                                           1-backyields.GetTransFactAlt(lepton, regionName, "Wjets"), 
                                                           "user","userOverallSys"))
        
        
        
        region.getSample("gammajets").addSystematic(Systematic("matMu",
                                                               configMgr.weights, 
                                                               1+backyields.GetMatrixUpAlt(lepton, regionName, "gammajets"), 
                                                               1+backyields.GetMatrixDownAlt(lepton, regionName, "gammajets"), 
                                                               "user","userOverallSys"))

## Discovery fit
if myFitType == FitType.Discovery: 

    print "In Discovery"

    discovery = configMgr.addTopLevelXMLClone(bkgOnly,"SimpleChannel_Discovery")
    #discovery.clearSystematics()
    sigSample = Sample("discoveryMode",kBlue)
    sigSample.setNormFactor("mu_SIG",0.5,0.,1.)
    sigSample.setNormByTheory()
    discovery.addSamples(sigSample)
    discovery.setSignalSample(sigSample)

    sigSample.buildHisto([1.0], "SRWEl", "cuts")
    sigSample.buildHisto([1.0], "SRWMu", "cuts")
    sigSample.buildHisto([0.0], "WCRhHT", "cuts")

#"SU_350_300_0_10","SU_500_450_0_10","SU_700_650_0_10","SU_800_750_0_10",,"SU_1000_950_0_10","SU_1150_1100_0_10","SU_1200_1150_0_10",
# sigSamples = ["wino_1500_100", "wino_1500_150", "wino_1500_200", "wino_1500_250", "wino_1500_300", "wino_1500_350",
#               "wino_1000_100", "wino_1000_150", "wino_1000_200", "wino_1000_250", "wino_1000_300", "wino_1000_350",
#               "wino_900_100", "wino_900_150", "wino_900_200", "wino_900_250", "wino_900_300", "wino_900_350",
#               "wino_800_100", "wino_800_150", "wino_800_200", "wino_800_250", "wino_800_300", "wino_800_350",
#               "wino_800_400", "wino_800_500", "wino_800_600", "wino_800_700", "wino_800_780",
#               "wino_700_100", "wino_700_150", "wino_700_200", "wino_700_250", "wino_700_300", "wino_700_350",
#               "wino_700_400", "wino_700_500", "wino_700_600", "wino_700_680",
#               "wino_600_100", "wino_600_200", "wino_600_300", "wino_600_400", "wino_600_500", "wino_600_580"]


if myFitType == FitType.Exclusion:

    #sigSamples = ["wino_400"]
    sigSamples = ["wino_100", "wino_150", "wino_200", "wino_250", "wino_300", "wino_350", "wino_400", "wino_450", "wino_500"]

    for sig in sigSamples:
        myTopLvl = configMgr.addTopLevelXMLClone(bkgOnly,"SimpleChannel_%s"%sig) #This is cloning the fit such that the systematics are also considered for the signal
        relUnc = theoryUnc[sig]
        sigSample = Sample(sig,kRed)
    #    sigSample.setNormFactor("mu_SIG",1.,0.,500.)
    #    sigSample.setNormFactor("mu_SIG",0.5,0.,1.)
        sigSample.setNormFactor("mu_SIG",1.,0.,5.)
        sigSample.setStatConfig(True)

        # Decide whether to add theory systematics or not:
        sigSample.setNormByTheory()

        if mode == '_NoTheoryUncertsXsecNominal':
            sigma = 0.0
        elif mode == '_NoTheoryUncertsXsecMinus1Sigma':
            sigma = -1.0
        elif mode == '_NoTheoryUncertsXsecPlus1Sigma':
            sigma = 1.0
        else:
            print "***ERROR: mode not supported:",mode
            exit(1)



        print "about to build histos:",sig
        for lepton in ('El', 'Mu'):
            for region in ("WCRhHT", "HMEThHT", "HMThHT", "SRW"):
                regionName = region+lepton
                if regionName == 'WCRhHTEl':
                    regionName = 'WCRhHT'
                elif regionName == 'WCRhHTMu':
                    continue
                sigSample.buildHisto([winoyields.GetYield(lepton, region, sig) * (1.0+sigma*relUnc)], regionName, "cuts")
                sigSample.buildStatErrors([winoyields.GetYieldUnc(lepton, region, sig) * (1.0+sigma*relUnc)], regionName, "cuts")

        myTopLvl.addSamples(sigSample)
        myTopLvl.setSignalSample(sigSample)
        #myTopLvl.setSignalChannels([SRWEl, SRWMu]) # do I need to do this again?


        for regionAlt in elChannels + muChannels:
            
            # now get the region from this clone
            region = myTopLvl.getChannelByName(regionAlt.name)
            
            regionName = region.name[5:-2]
            lepton = region.name[-2:]

            if lepton == 'HT':
                lepton = 'El'
                regionName = region.name[5:]


            region.getSample(sig).addSystematic(Systematic("pileup",
                                                           configMgr.weights, 
                                                           1+winoyields.GetPileUp(lepton, regionName, sig), 
                                                           1+winoyields.GetPileDown(lepton, regionName, sig), 
                                                           "user","userOverallSys"))

            region.getSample(sig).addSystematic(Systematic("jes",
                                                           configMgr.weights, 
                                                           1+winoyields.GetJESUp(lepton, regionName, sig), 
                                                           1+winoyields.GetJESDown(lepton, regionName, sig), 
                                                           "user","userOverallSys"))

            region.getSample(sig).addSystematic(Systematic("jer",
                                                           configMgr.weights, 
                                                           1+winoyields.GetJER(lepton, regionName, sig), 
                                                           1-winoyields.GetJER(lepton, regionName, sig), 
                                                           "user","userOverallSys"))

            region.getSample(sig).addSystematic(Systematic("muonScale",
                                                           configMgr.weights, 
                                                           1+winoyields.GetMuonScaleUp(lepton, regionName, sig), 
                                                           1+winoyields.GetMuonScaleDown(lepton, regionName, sig), 
                                                           "user","userOverallSys"))
            
            region.getSample(sig).addSystematic(Systematic("muonMSRes",
                                                           configMgr.weights, 
                                                           1+winoyields.GetMuonMSRes(lepton, regionName, sig)/2.0, 
                                                           1-winoyields.GetMuonMSRes(lepton, regionName, sig)/2.0, 
                                                           "user","userOverallSys"))
            
            region.getSample(sig).addSystematic(Systematic("muonIDRes",
                                                           configMgr.weights, 
                                                           1+winoyields.GetMuonIDRes(lepton, regionName, sig)/2.0, 
                                                           1-winoyields.GetMuonIDRes(lepton, regionName, sig)/2.0, 
                                                           "user","userOverallSys"))

            region.getSample(sig).addSystematic(Systematic("egScale",
                                                           configMgr.weights, 
                                                           1+winoyields.GetEgScaleUp(lepton, regionName, sig), 
                                                           1+winoyields.GetEgScaleDown(lepton, regionName, sig), 
                                                           "user","userOverallSys"))
            
            region.getSample(sig).addSystematic(Systematic("egPS",
                                                           configMgr.weights, 
                                                           1+winoyields.GetEgPSUp(lepton, regionName, sig), 
                                                           1+winoyields.GetEgPSDown(lepton, regionName, sig), 
                                                           "user","userOverallSys"))
            
            region.getSample(sig).addSystematic(Systematic("egMaterial",
                                                           configMgr.weights, 
                                                           1+winoyields.GetEgMatUp(lepton, regionName, sig), 
                                                           1+winoyields.GetEgMatDown(lepton, regionName, sig), 
                                                           "user","userOverallSys"))
            
            region.getSample(sig).addSystematic(Systematic("egRes",
                                                           configMgr.weights, 
                                                           1+winoyields.GetEgResUp(lepton, regionName, sig), 
                                                           1+winoyields.GetEgResDown(lepton, regionName, sig), 
                                                           "user","userOverallSys"))


# These lines are needed for the user analysis to run
# Make sure file is re-made when executing HistFactory
if configMgr.executeHistFactory:
    if os.path.isfile("data/%s.root"%configMgr.analysisName):
        os.remove("data/%s.root"%configMgr.analysisName) 
