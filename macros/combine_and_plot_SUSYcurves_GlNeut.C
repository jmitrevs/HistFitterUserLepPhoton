#include <vector>
#include <iostream>
#include <TGraph.h>
#include <TLatex.h>
#include <TCanvas.h>
#include <TColor.h>
#include <TFile.h>
#include <TH2F.h>
#include <TLegend.h>

vector<TGraph*> contoursToGraphs(TObjArray *conts, Int_t color, Int_t width, Int_t style) {
  vector<TGraph*> outputGraphs;
  Double_t x1[1000];
  Double_t y1[1000];
  Int_t nGraphs    = 0;
  Int_t TotalConts = 0;
  TList* contLevel = NULL;
  TGraph* curv     = NULL;
  TGraph* gc       = NULL;
  if (conts == NULL){
     printf("*** No Contours Were Extracted!\n");
     TotalConts = 0;
     return;
  } else {
     TotalConts = conts->GetSize();
  }

  // There should only be one contour level, else they weren't set right
  printf("TotalConts = %d; this number should be 1\n", TotalConts);
  Int_t npoints = 0;
  Double_t x0,y0,z0;
  contour = (TList*)conts->At(0);
  printf("Contour has %d graphs\n", contour->GetSize());
  curv = (TGraph*)contour->First();
  for(Int_t j = 0; j < contour->GetSize(); j++) {
//     curv->GetPoint(0, x0, y0);
     nGraphs++;
     printf("\tGraph: %d  -- %d Elements\n", nGraphs,curv->GetN());
     gc = (TGraph*)curv->Clone();
     gc->SetLineColor(color);
     gc->SetLineWidth(width);
     gc->SetLineStyle(style);
     outputGraphs.push_back(gc);        
     curv = (TGraph*)contour->After(curv); // Get Next graph     
  }
  cout << "Really almost done" << endl;
  return outputGraphs;
};

void combine_and_plot_SUSYcurves_GlNeut_Sept9()
{
  gROOT->LoadMacro("AtlasStyle.C");
  SetAtlasStyle();

  Double_t contourLevel[1];
  contourLevel[0] = 1.0;
  
  TCanvas *c1 = new TCanvas();
  //  c1->SetGridx();
  //  c1->SetGridy();

  Int_t c_myYellow   = TColor::GetColor("#ffe938"); // TColor::GetColor( "#fee000" )
  Int_t c_myRed      = TColor::GetColor("#aa000");

  TLegend *leg = new TLegend(0.225,0.51,0.55,0.71);
  leg->SetFillColor(0);
  leg->SetBorderSize(0);

  TFile *fileNoTheoryUncertsXsecNominal = new TFile("MyGGMAnalysisGlNeut_NoTheoryUncertsXsecNominal_Output_upperlimit__1_harvest_list.root");
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

  TH2F *hObsNoTheoryUncertsXsecNominal = upperLimit->Clone("hObsNoTheoryUncertsXsecNominal");
  hObsNoTheoryUncertsXsecNominal->SetLineStyle(1);
  hObsNoTheoryUncertsXsecNominal->SetLineWidth(4);
  hObsNoTheoryUncertsXsecNominal->SetLineColor(c_myRed);
  hObsNoTheoryUncertsXsecNominal->SetContour(1, contourLevel);
  hObsNoTheoryUncertsXsecNominal->GetXaxis()->SetTitle("neutralino mass [GeV]");
  hObsNoTheoryUncertsXsecNominal->GetYaxis()->SetTitle("gluino mass [GeV]");

  TFile *fileNoTheoryUncertsXsecPlus1Sigma = new TFile("MyGGMAnalysisGlNeut_NoTheoryUncertsXsecPlus1Sigma_Output_upperlimit__1_harvest_list.root");
  TH2F *hObsNoTheoryUncertsXsecPlus1Sigma = upperLimit->Clone("hObsNoTheoryUncertsXsecPlus1Sigma");
  hObsNoTheoryUncertsXsecPlus1Sigma->SetLineStyle(2);
  hObsNoTheoryUncertsXsecPlus1Sigma->SetLineWidth(2);
  hObsNoTheoryUncertsXsecPlus1Sigma->SetLineColor(c_myRed);
  hObsNoTheoryUncertsXsecPlus1Sigma->SetContour(1, contourLevel);

  TFile *fileNoTheoryUncertsXsecMinus1Sigma = new TFile("MyGGMAnalysisGlNeut_NoTheoryUncertsXsecMinus1Sigma_Output_upperlimit__1_harvest_list.root");
  TH2F *hObsNoTheoryUncertsXsecMinus1Sigma = upperLimit->Clone("hObsNoTheoryUncertsXsecMinus1Sigma");
  hObsNoTheoryUncertsXsecMinus1Sigma->SetLineStyle(2);
  hObsNoTheoryUncertsXsecMinus1Sigma->SetLineWidth(2);
  hObsNoTheoryUncertsXsecMinus1Sigma->SetLineColor(c_myRed);
  hObsNoTheoryUncertsXsecMinus1Sigma->SetContour(1, contourLevel);
  
//  hObsNoTheoryUncertsXsecNominal->Draw("cont3");
  hObsNoTheoryUncertsXsecNominal->Draw("cont list");
  c1->Update();
  TObjArray *conts = (TObjArray*)gROOT->GetListOfSpecials()->FindObject("contours");
  vector<TGraph*> obsCurves = contoursToGraphs(conts, c_myRed, 4, 1);
  cout << "Size of obsCurves is " << obsCurves.size() << endl;
  Double_t xobs[100];
  Double_t yobs[100];
  Int_t npoints=0;
  cout << (obsCurves[0]->GetN())-1 << endl;
  for (Int_t ipoint = (obsCurves[0]->GetN())-1; ipoint > -1; ipoint--) {
     cout << (obsCurves[0]->GetX())[ipoint] << ", " 
          << (obsCurves[0]->GetY())[ipoint] << endl;
     Double_t slope = ((obsCurves[0]->GetY())[ipoint] - (obsCurves[0]->GetY())[ipoint+1])/
        ((obsCurves[0]->GetX())[ipoint] - (obsCurves[0]->GetX())[ipoint+1]);
     if (ipoint==(obsCurves[0]->GetN())-1 || slope>0) {
        cout << "Keep the point above" << endl;
        xobs[npoints] = (obsCurves[0]->GetX())[ipoint];
        yobs[npoints] = (obsCurves[0]->GetY())[ipoint];
        npoints++;
     } else {
        break;
     }
  }
  cout << "Got " << npoints << " points" << endl;
  xobs[npoints]=xobs[npoints-1]+10.;
  yobs[npoints]=1090.;
  npoints++;
  TGraph *obs0 = new TGraph(npoints, xobs, yobs);
  obs0->SetLineColor(c_myRed);
  obs0->SetLineWidth(4);

  cout << "Now working on Obs +1sigma curve" << endl;
  hObsNoTheoryUncertsXsecPlus1Sigma->Draw("cont list");
  c1->Update();
  TObjArray *conts = (TObjArray*)gROOT->GetListOfSpecials()->FindObject("contours");
  vector<TGraph*> obsp1Curves = contoursToGraphs(conts, c_myRed, 2, 2);
  obsp1Curves[1]->Draw();
  Double_t xobsp1[100];
  Double_t yobsp1[100];
  npoints=0;
  for (Int_t ipoint = (obsp1Curves[0]->GetN())-1; ipoint > -1; ipoint--) {
     cout << (obsp1Curves[0]->GetX())[ipoint] << ", " 
          << (obsp1Curves[0]->GetY())[ipoint] << endl;
     Double_t slope = ((obsp1Curves[0]->GetY())[ipoint] - (obsp1Curves[0]->GetY())[ipoint+1])/
        ((obsp1Curves[0]->GetX())[ipoint] - (obsp1Curves[0]->GetX())[ipoint+1]);
     if (ipoint==0 || slope>0) {
        cout << "Keep the point above" << endl;
        xobsp1[npoints] = (obsp1Curves[0]->GetX())[ipoint];
        yobsp1[npoints] = (obsp1Curves[0]->GetY())[ipoint];
        npoints++;
     } else {
        break;
     }
  }
  cout << "Got " << npoints << " points" << endl;
  xobsp1[npoints]=xobsp1[npoints-1]+10.;
  yobsp1[npoints]=1090.;
  npoints++;
  TGraph *obsp10 = new TGraph(npoints, xobsp1, yobsp1);
  obsp10->SetLineColor(c_myRed);
  obsp10->SetLineStyle(2);
  obsp10->SetLineWidth(2);

  cout << "Now working on Obs -1sigma curve" << endl;
  hObsNoTheoryUncertsXsecMinus1Sigma->Draw("cont list");
  c1->Update();
  TObjArray *conts = (TObjArray*)gROOT->GetListOfSpecials()->FindObject("contours");
  vector<TGraph*> obsm1Curves = contoursToGraphs(conts, c_myRed, 2, 2);
  obsm1Curves[0]->Draw();
  obsm1Curves[2]->Draw();
  Double_t xobsm1[100];
  Double_t yobsm1[100];
  npoints=0;
  for (Int_t ipoint = (obsm1Curves[1]->GetN())-1; ipoint > -1; ipoint--) {
     cout << (obsm1Curves[1]->GetX())[ipoint] << ", " 
          << (obsm1Curves[1]->GetY())[ipoint] << endl;
     Double_t slope = ((obsm1Curves[1]->GetY())[ipoint] - (obsm1Curves[1]->GetY())[ipoint+1])/
        ((obsm1Curves[1]->GetX())[ipoint] - (obsm1Curves[1]->GetX())[ipoint+1]);
     if (ipoint==0 || slope>0) {
        cout << "Keep the point above" << endl;
        xobsm1[npoints] = (obsm1Curves[1]->GetX())[ipoint];
        yobsm1[npoints] = (obsm1Curves[1]->GetY())[ipoint];
        npoints++;
     } else {
        break;
     }
  }
  cout << "Got " << npoints << " points" << endl;
  xobsm1[npoints]=xobsm1[npoints-1]+10.;
  yobsm1[npoints]=1090.;
  npoints++;
  TGraph *obsm11 = new TGraph(npoints, xobsm1, yobsm1);
  obsm11->SetLineColor(c_myRed);
  obsm11->SetLineStyle(2);
  obsm11->SetLineWidth(2);

  hExpNoTheoryUncertsXsecNominal->Draw("cont list");
  c1->Update();
  TObjArray *conts = (TObjArray*)gROOT->GetListOfSpecials()->FindObject("contours");
  vector<TGraph*> expCurves = contoursToGraphs(conts, kBlack, 2, 2);
  Double_t xexp[100];
  Double_t yexp[100];
  npoints=0;
  for (Int_t ipoint = (expCurves[0]->GetN())-1; ipoint > -1; ipoint--) {
     // cout << "ipoint=" << ipoint << endl;
     // cout << (expCurves[0]->GetX())[ipoint] << ", " 
     //      << (expCurves[0]->GetY())[ipoint] << endl;
     Double_t slope = 0;
     if (ipoint < (expCurves[0]->GetN())-1) {
        slope = ((expCurves[0]->GetY())[ipoint] - (expCurves[0]->GetY())[ipoint+1])/
           ((expCurves[0]->GetX())[ipoint] - (expCurves[0]->GetX())[ipoint+1]);
     }
     if (ipoint==(expCurves[0]->GetN())-1 || slope>0) {
        // cout << "Keep the point above" << endl;
        xexp[npoints] = (expCurves[0]->GetX())[ipoint];
        yexp[npoints] = (expCurves[0]->GetY())[ipoint];
        npoints++;
     } else {
        break;
     }
  }
  cout << "Got " << npoints << " points" << endl;
  xexp[npoints]=xexp[npoints-1]+10.;
  yexp[npoints]=1090.;
  npoints++;
  TGraph *exp0 = new TGraph(npoints, xexp, yexp);
  exp0->SetLineStyle(2);
  exp0->SetLineWidth(2);
  exp0->SetLineColor(1);

  hExpPlus1NoTheoryUncertsXsecNominal->Draw("cont list");
  c1->Update();
  TObjArray *conts = (TObjArray*)gROOT->GetListOfSpecials()->FindObject("contours");
  vector<TGraph*> expp1Curves = contoursToGraphs(conts, c_myYellow, 2, 2);
  cout << "Found " << expp1Curves.size() << " curves" << endl;
  Double_t xexpp1[100];
  Double_t yexpp1[100];
  npoints=0;
  for (Int_t ipoint = (expp1Curves[1]->GetN())-1; ipoint > -1; ipoint--) {
     // cout << (expp1Curves[1]->GetX())[ipoint] << ", " 
     //      << (expp1Curves[1]->GetY())[ipoint] << endl;
     Double_t slope = 0; 
     if (ipoint < (expp1Curves[1]->GetN())-1) {
        slope = ((expp1Curves[1]->GetY())[ipoint] - (expp1Curves[1]->GetY())[ipoint+1])/
           ((expp1Curves[1]->GetX())[ipoint] - (expp1Curves[1]->GetX())[ipoint+1]);
     }
     if (ipoint==(expp1Curves[1]->GetN())-1 || slope>0) {
        // cout << "Keep the point above" << endl;
        xexpp1[npoints] = (expp1Curves[1]->GetX())[ipoint];
        yexpp1[npoints] = (expp1Curves[1]->GetY())[ipoint];
        npoints++;
     } else {
        break;
     }
  }
  cout << "Got " << npoints << " points" << endl;
  xexpp1[npoints]=xexpp1[npoints-1]+10.;
  yexpp1[npoints]=1090.;
  npoints++;
  xexpp1[npoints]=160.;
  yexpp1[npoints]=1090;
  npoints++;

  TGraph *expp11 = new TGraph(npoints, xexpp1, yexpp1);
  expp11->SetLineStyle(2);
  expp11->SetLineColor(c_myYellow);
  expp11->SetLineWidth(2);
  expp11->SetFillColor(c_myYellow);

  Double_t xexp2[100];
  Double_t yexp2[100];
  npoints=0;
  for (Int_t ipoint=0; ipoint<expp1Curves[2]->GetN(); ipoint++) {
     xexp2[npoints]=(expp1Curves[2]->GetX())[ipoint];
     yexp2[npoints]=(expp1Curves[2]->GetY())[ipoint];
     cout << xexp2[npoints] << "," << yexp2[npoints] << endl;
     npoints++;
  }

  hExpMinus1NoTheoryUncertsXsecNominal->Draw("cont list");
  c1->Update();
  TObjArray *conts = (TObjArray*)gROOT->GetListOfSpecials()->FindObject("contours");
  vector<TGraph*> expm1Curves = contoursToGraphs(conts, c_myYellow, 2, 2);
  // cout << "Found " << expm1Curves.size() << " curves" << endl;
  for (Int_t ipoint = (expm1Curves[0]->GetN())-1; ipoint > -1; ipoint--) {
     xexp2[npoints]=(expm1Curves[0]->GetX())[ipoint];
     yexp2[npoints]=(expm1Curves[0]->GetY())[ipoint];
     // cout << xexp2[npoints] << "," << yexp2[npoints] << endl;
     npoints++;
  }
  cout << "Got " << npoints << " points" << endl;
  // These belong to the piece running at high gluino mass
  TGraph *exppm2 = new TGraph(npoints, xexp2, yexp2);
  exppm2->SetFillColor(c_myYellow);

  hExpMinus1NoTheoryUncertsXsecNominal->Draw("cont3");
  hExpMinus1NoTheoryUncertsXsecNominal->GetXaxis()->SetTitle("neutralino mass [GeV]");
  hExpMinus1NoTheoryUncertsXsecNominal->GetYaxis()->SetTitle("gluino mass [GeV]");
  expp1Curves[0]->SetFillColor(c_myYellow);
  expCurves[1]->SetLineColor(1);

  expp11->Draw("lf");
  exppm2->Draw("lf");
  expp1Curves[0]->Draw("lf");
  expCurves[1]->Draw();
  exp0->Draw();
  
  obsCurves[1]->Draw();
  obs0->Draw();
  obsp1Curves[2]->Draw();
  obsp10->Draw();
  obsm1Curves[0]->Draw();
  obsm1Curves[2]->Draw();
  obsm11->Draw();

  Double_t forbiddenx[4] = {200.,1050.,1050.,200.};
  Double_t forbiddeny[4] = {200.,1050.,200.,200.};
  TGraph *forbidden = new TGraph(4, forbiddenx, forbiddeny); 
  forbidden->SetFillColor(kGray);
  forbidden->Draw("f");

  leg->SetTextSize( 0.04 );
//  leg->SetTextFont( 42 );
  leg->AddEntry(hObsNoTheoryUncertsXsecNominal, "Observed limit (#pm1 #sigma^{SUSY}_{theory})", "l");
  TGraph* gr_temp = new TGraph();
  gr_temp->SetFillColor(c_myYellow);
  gr_temp->SetFillStyle(1001);
  gr_temp->SetLineColor(1);
  gr_temp->SetLineStyle(2);
  gr_temp->SetLineWidth(2);
  leg->AddEntry(gr_temp,"Expected limit (#pm1 #sigma_{exp})","LF");
  leg->Draw();

  TLine obssigma;
  obssigma.SetLineStyle(2);
  obssigma.SetLineColor(c_myRed);
  obssigma.SetLineWidth(2);

  float x1 = leg->GetX1();
  float x2 = leg->GetX2();
  float y1 = leg->GetY1();
  float y2 = leg->GetY2();
  float legwidth = x2-x1;
  float legheight = y2-y1;

  obssigma.DrawLineNDC(x1+0.04*legwidth,y2-0.10*legheight,x1+0.213*legwidth,y2-0.10*legheight);
  obssigma.DrawLineNDC(x1+0.04*legwidth,y2-0.39*legheight,x1+0.213*legwidth,y2-0.39*legheight);

  TLatex l; //l.SetTextAlign(12); l.SetTextSize(tsize); 
  l.SetNDC();
  l.SetTextFont(72);
  l.SetTextColor(kBlack);
  l.DrawLatex(0.66,0.48,"ATLAS Internal");
  l.SetTextFont(42);
  l.DrawLatex(0.66,0.36,"#int Ldt = 4.7 fb^{-1}");
  l.DrawLatex(0.66,0.26,"#sqrt{s}=7 TeV");
  l.DrawLatex(0.2,0.96,"GGM: higgsino-like neutralino, tan#beta=1.5, |#mu|<0");
  l.DrawLatex(0.35,0.2,"#tilde{g} NLSP");

  l.SetTextSize(0.035);
  l.DrawLatex(0.24,0.46,"All limits at 95% CL");

}

