
#include "TString.h"

void makelistfiles()
{
  gSystem->Load("libSusyFitter.so");

  // input root file with HypoTestInverterResults, 
  // as obtained from running: 
  // HistFitter.py -l python/MyGGMAnalysis.py
  //const char* inputfile  = "results/LepPhoton_AllUncertsXsecNominal_AnalysisOutput_upperlimit.root";
  //const char* inputfile  = "results/LepPhoton_AllUncertsXsecMinus1Sigma_AnalysisOutput_upperlimit.root";
  //const char* inputfile  = "results/LepPhoton_AllUncertsXsecPlus1Sigma_AnalysisOutput_upperlimit.root";
  //

  //const char* inputfile  = "results/LepPhoton8TeV_weak_NoTheoryUncertsXsecNominal_AnalysisOutput_hypotest.root";
  //const char* inputfile  = "results/LepPhoton8TeV_weak_NoTheoryUncertsXsecMinus1Sigma_AnalysisOutput_hypotest.root";
  //const char* inputfile  = "results/LepPhoton8TeV_weak_NoTheoryUncertsXsecPlus1Sigma_AnalysisOutput_hypotest.root";

  //const char* inputfile  = "results/LepPhoton8TeV_weak_NoTheoryUncertsXsecMinus1Sigma_AnalysisOutput_upperlimit.root";
  //const char* inputfile  = "results/LepPhoton8TeV_weak_NoTheoryUncertsXsecPlus1Sigma_AnalysisOutput_upperlimit.root";

  const char* inputfile  = "results/LepPhoton8TeV_weak_NoTheoryUncertsXsecNominal_AnalysisOutput_upperlimit.root";
  // const char* inputfile  = "results/LepPhoton8TeV_weak_NoTheoryUncertsXsecNominal_electron_AnalysisOutput_upperlimit.root";
  //const char* inputfile  = "results/LepPhoton8TeV_weak_NoTheoryUncertsXsecNominal_muon_AnalysisOutput_upperlimit.root";
  //const char* inputfile  = "results/LepPhoton8TeV_test_NoTheoryUncertsXsecNominal_AnalysisOutput_upperlimit.root";


  // search for objects labelled
  // If you have two subprocesses, it seems to use the second name
  const char* format     = "hypo_wino_%f";
  // interpret %f's above respectively as (separated by ':')
  const char* interpretation = "mwino";
  //  const char* interpretation = "n";
  // cut string on m0 and m12 value, eg "m0>1200"
  const char* cutStr = "1"; // accept everything

  TString outputfile = CollectAndWriteHypoTestResults( inputfile, format, interpretation, cutStr ) ;

  // load the listfile in root with:
  // root -l summary_harvest_tree_description.h
  // or look directly at the outputfile in vi.
}

