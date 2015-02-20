#include "macros/m_vs_mN_nofloat.C"

void makecontourhists(const TString& combo = "all" /*"0lepton"*/ /*"1lepton"*/) 
{
  // const char* ehistfile = m_vs_mN_nofloat("LepPhoton_AllUncertsXsecNominal_AnalysisOutput_upperlimit__1_harvest_list");
  // const char* ehistfile = m_vs_mN_nofloat("LepPhoton_AllUncertsXsecMinus1Sigma_AnalysisOutput_upperlimit__1_harvest_list");
  // const char* ehistfile = m_vs_mN_nofloat("LepPhoton_AllUncertsXsecPlus1Sigma_AnalysisOutput_upperlimit__1_harvest_list");
  // const char* ehistfile = m_vs_mN_nofloat("LepPhoton_NoTheoryUncertsXsecNominal_AnalysisOutput_upperlimit__1_harvest_list");
  // const char* ehistfile = m_vs_mN_nofloat("LepPhoton_NoTheoryUncertsXsecMinus1Sigma_AnalysisOutput_upperlimit__1_harvest_list");
  // const char* ehistfile = m_vs_mN_nofloat("LepPhoton_NoTheoryUncertsXsecPlus1Sigma_AnalysisOutput_upperlimit__1_harvest_list");
  const char* ehistfile = m_vs_mN_nofloat("LepPhoton8TeV_weak_NoTheoryUncertsXsecNominal_AnalysisOutput_hypotest__1_harvest_list");
  const char* ehistfile = m_vs_mN_nofloat("LepPhoton8TeV_weak_NoTheoryUncertsXsecMinus1Sigma_AnalysisOutput_hypotest__1_harvest_list");
  const char* ehistfile = m_vs_mN_nofloat("LepPhoton8TeV_weak_NoTheoryUncertsXsecPlus1Sigma_AnalysisOutput_hypotest__1_harvest_list");
}



