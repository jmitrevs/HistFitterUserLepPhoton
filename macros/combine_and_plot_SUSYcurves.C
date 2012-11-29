void combine_and_plot_SUSYcurves()
{

  gROOT->LoadMacro("AtlasStyle.C");
  SetAtlasStyle();

  Double_t contourLevel[1];
  contourLevel[0] = 1.0;
  
  TCanvas *c1 = new TCanvas();
  c1->SetGridx();
  c1->SetGridy();

  Int_t c_myYellow   = TColor::GetColor("#ffe938");
  Int_t c_myRed      = TColor::GetColor("#aa000");

  TLegend *leg = new TLegend(0.5,0.65,0.9,0.9);
  leg->SetFillColor(0);
  leg->SetBorderSize(0);

  TFile *fileAllUncertsXsecNominal = new TFile("LepPhoton_AllUncertsXsecNominal_AnalysisOutput_upperlimit__1_harvest_list.root");
  TH2F *hObsAllUncertsXsecNominal = upperLimit->Clone("hObsAllUncertsXsecNominal");
  hObsAllUncertsXsecNominal->SetLineStyle(1);
  hObsAllUncertsXsecNominal->SetLineWidth(4);
  hObsAllUncertsXsecNominal->SetLineColor(c_myRed);
  hObsAllUncertsXsecNominal->SetContour(1, contourLevel);
  hObsAllUncertsXsecNominal->GetXaxis()->SetTitle("neutralino mass [GeV]");
  hObsAllUncertsXsecNominal->GetYaxis()->SetTitle("gluino mass [GeV]");

  TFile *fileAllUncertsXsecPlus1Sigma = new TFile("LepPhoton_AllUncertsXsecPlus1Sigma_AnalysisOutput_upperlimit__1_harvest_list.root");
  TH2F *hObsAllUncertsXsecPlus1Sigma = upperLimit->Clone("hObsAllUncertsXsecPlus1Sigma");
  hObsAllUncertsXsecPlus1Sigma->SetLineStyle(2);
  hObsAllUncertsXsecPlus1Sigma->SetLineWidth(2);
  hObsAllUncertsXsecPlus1Sigma->SetLineColor(c_myRed);
  hObsAllUncertsXsecPlus1Sigma->SetContour(1, contourLevel);

  TFile *fileAllUncertsXsecMinus1Sigma = new TFile("LepPhoton_AllUncertsXsecMinus1Sigma_AnalysisOutput_upperlimit__1_harvest_list.root");
  TH2F *hObsAllUncertsXsecMinus1Sigma = upperLimit->Clone("hObsAllUncertsXsecMinus1Sigma");
  hObsAllUncertsXsecMinus1Sigma->SetLineStyle(2);
  hObsAllUncertsXsecMinus1Sigma->SetLineWidth(2);
  hObsAllUncertsXsecMinus1Sigma->SetLineColor(c_myRed);
  hObsAllUncertsXsecMinus1Sigma->SetContour(1, contourLevel);
  
  TFile *fileNoTheoryUncertsXsecNominal = new TFile("LepPhoton_NoTheoryUncertsXsecNominal_AnalysisOutput_upperlimit__1_harvest_list.root");
  TH2F *hExpNoTheoryUncertsXsecNominal = expectedUpperLimit->Clone("hExpNoTheoryUncertsXsecNominal");
  TH2F *hExpPlus1NoTheoryUncertsXsecNominal = expectedUpperLimitPlus1Sig->Clone("hExpPlus1NoTheoryUncertsXsecNominal");
  TH2F *hExpMinus1NoTheoryUncertsXsecNominal = expectedUpperLimitMinus1Sig->Clone("hExpMinus1NoTheoryUncertsXsecNominal");
  hExpNoTheoryUncertsXsecNominal->SetLineStyle(2);
  hExpNoTheoryUncertsXsecNominal->SetLineColor(kBlack);
  hExpPlus1NoTheoryUncertsXsecNominal->SetLineStyle(1);
  hExpPlus1NoTheoryUncertsXsecNominal->SetLineColor(c_myYellow);
  hExpMinus1NoTheoryUncertsXsecNominal->SetLineStyle(1);
  hExpMinus1NoTheoryUncertsXsecNominal->SetLineColor(c_myYellow);

  hExpNoTheoryUncertsXsecNominal->SetContour(1, contourLevel);
  hExpPlus1NoTheoryUncertsXsecNominal->SetContour(1, contourLevel);
  hExpMinus1NoTheoryUncertsXsecNominal->SetContour(1, contourLevel);

  TH2F *hFrame = new TH2F("frame", "frame;neutralino mass [GeV];gluino mass [GeV]", 100, 100, 800, 100, 500, 1500);
  hFrame->Draw();

  hObsAllUncertsXsecNominal->Draw("cont3 same");
  hObsAllUncertsXsecPlus1Sigma->Draw("cont3 same");
  hObsAllUncertsXsecMinus1Sigma->Draw("cont3 same");
  hExpNoTheoryUncertsXsecNominal->Draw("cont3 same");
  hExpPlus1NoTheoryUncertsXsecNominal->Draw("cont3 same");
  hExpMinus1NoTheoryUncertsXsecNominal->Draw("cont3 same");

  leg->AddEntry(hObsAllUncertsXsecNominal, "Observed Limit w/ Theory Uncerts", "l");
  leg->AddEntry(hObsAllUncertsXsecMinus1Sigma, "Observed Limit w/ #pm 1#sigma Theory Uncerts", "l");
  leg->AddEntry(hExpNoTheoryUncertsXsecNominal, "Expected Limit w/o Theory Uncerts", "l");
  leg->AddEntry(hExpMinus1NoTheoryUncertsXsecNominal, "#pm 1#sigma Expected w/o Theory Uncerts", "lf");

  //  hObsAllUncertsXsecPlus1Sigma->SetMarkerSize(1.0);
  //  hObsAllUncertsXsecNominal->Draw("text same");

  Double_t forbiddenx[4] = {200.,1050.,1050.,200.};
  Double_t forbiddeny[4] = {200.,1050.,200.,200.};
  TGraph *forbidden = new TGraph(4, forbiddenx, forbiddeny); 
  forbidden->SetFillColor(kGray);
  forbidden->SetLineColor(kGray);
  forbidden->Draw("f");

  leg->Draw();

  TLatex l; //l.SetTextAlign(12); l.SetTextSize(tsize); 
  l.SetNDC();
  l.SetTextFont(72);
  l.SetTextColor(kBlack);
  l.DrawLatex(0.5,0.57,"ATLAS Internal");
  l.SetTextFont(42);
  l.DrawLatex(0.5,0.47,"#int Ldt = 4.7-4.8 fb^{-1}");
  l.DrawLatex(0.5,0.37,"#sqrt{s}=7 TeV");
  l.DrawLatex(0.2,0.96,"GGM: wino-like neutralino");
  //l.DrawLatex(0.35,0.2,"#tilde{g} NLSP");

}
