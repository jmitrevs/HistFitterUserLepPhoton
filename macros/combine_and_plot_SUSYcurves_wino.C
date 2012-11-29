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
     nGraphs++;
     curv->GetPoint(0, x0, y0);

     const Int_t N = curv->GetN();
     printf("\tGraph: %d  -- %d Elements, x0 = %g, y0 = %g\n", N, x0, y0);

     Double_t xNew[120], yNew[120];
     points = 0;
     for (int i = 0; i < N; i++) {
       curv->GetPoint(i, x0, y0);
       if (y0 - x0 > 30) {
	 xNew[points] = x0;
	 yNew[points++] = y0;
       }
     }
     gc = new TGraph(points, xNew, yNew);
     gc->SetLineColor(color);
     gc->SetLineWidth(width);
     gc->SetLineStyle(style);
     outputGraphs.push_back(gc);        
     curv = (TGraph*)contour->After(curv); // Get Next graph     
  }
  cout << "Really almost done" << endl;
  return outputGraphs;
};

TGraph* MergeTwoContours(TGraph* gr1, TGraph* gr2) {
  int number_of_bins = gr1->GetN()+gr2->GetN();

  const Int_t gr1N = gr1->GetN();
  const Int_t gr2N = gr2->GetN();

  const Int_t N = number_of_bins;
  Double_t x1[N], y1[N];

  cout << "Get the points in the first graph:" << endl;
  Double_t xx0, yy0;
  for(int j=0; j<gr1N; j++) {
    gr1->GetPoint(j,xx0,yy0);
    x1[j] = xx0;
    y1[j] = yy0;
    cout << "  point = (" << xx0 << ", " << yy0 << ")" << endl;
  }
  cout << "Get the points in the second graph:" << endl;
  for(int j=0; j<gr2N; j++) {
    gr2->GetPoint(j,xx0,yy0);
    x1[gr1N+j] = xx0;
    y1[gr1N+j] = yy0;
    cout << "  point = (" << xx0 << ", " << yy0 << ")" << endl;
  }

  gc = new TGraph(number_of_bins, x1, y1);
  return gc;
}

TGraph* FixContour(TGraph* gr1) {

  const Int_t gr1N = gr1->GetN();

  const Int_t N = gr1N;
  Double_t x1[N], y1[N];

  cout << "Get the points in the first graph:" << endl;
  Double_t xx0, yy0;
  for(int j=0; j<gr1N; j++) {
    gr1->GetPoint(j,xx0,yy0);
    x1[j] = xx0;
    if (j==0) {
      y1[j] = 1500.0;
    } else {
      y1[j] = yy0;
    }
    cout << "  point = (" << xx0 << ", " << yy0 << ")" << endl;
  }

  gc = new TGraph(N, x1, y1);
  return gc;
}

TGraph* MakeNewContour(TGraph* gr1) {

  const Int_t gr1N = gr1->GetN();

  const Int_t N = gr1N;
  Double_t x1[N], y1[N];

  cout << "Get the points in the first graph:" << endl;
  Double_t xx0, yy0;
  x1[0]=100;
  x1[0]=1500;
  for(int j=0; j<gr1N; j++) {
    gr1->GetPoint(j,xx0,yy0);
    x1[j] = 100;
    y1[j] = yy0;
    cout << "  point = (" << xx0 << ", " << yy0 << ")" << endl;
  }

  gc = new TGraph(N, x1, y1);
  return gc;
}

// This produces the shaded band for the expected limit systematics
TGraph* DrawExpectedBand(TGraph* gr1,  TGraph* gr2, Int_t fillColor, Int_t fillStyle,
			 double xlow, double xhigh, double ylow, double yhigh,
			 int cutx = 0, int cuty = 0) {

  int number_of_bins = max(gr1->GetN(),gr2->GetN());
  
  const Int_t gr1N = gr1->GetN();
  const Int_t gr2N = gr2->GetN();

  const Int_t N = number_of_bins;
  Double_t x1[N], y1[N], x2[N], y2[N];

  // Get the points in the first graph
  Double_t xx0, yy0;
  for(int j=0; j<gr1N; j++) {
    gr1->GetPoint(j,xx0,yy0);
      x1[j] = xx0;
      y1[j] = yy0;
  }
  if (gr1N < N) {
    for(int i=gr1N; i<N; i++) {
      x1[i] = x1[gr1N-1];
      y1[i] = y1[gr1N-1];
    }
  }

  // Get the points in the second graph
  Double_t xx1, yy1;
  for(int j=0; j<gr2N; j++) {
    gr2->GetPoint(j,xx1,yy1);
      x2[j] = xx1;
      y2[j] = yy1;
  }
  if (gr2N < N) {
    for(int i=gr2N; i<N; i++) {
      x2[i] = x2[gr2N-1];
      y2[i] = y2[gr2N-1];
    }      
  }
  
  // Prepare and fill the 2D region enclosed by the error band
  TGraph *grshade = new TGraph(2*N+10);

  int point = 0;
  double lastx = 0; // This is the last point in the first graph
  double lasty = 0;
  double firstx = -875; // This is the first point drawn in the first graph
  double firsty = -875; // Set an arbitrary initial value so we can check if it's filled!
  for (int i=0;i<N;i++) {
    if (x1[i] > cutx && y1[i] > cuty) { // Allow to exclude some points from being plotted
      grshade->SetPoint(point,x1[i],y1[i]);
      lastx = x1[i]; 
      lasty = y1[i]; 
      if(firstx == -875) {
		firstx = x1[i];
		firsty = y1[i];
      }
      point++;
    }
  }

  // Find the first point to be drawn in the second graph
  double nextx = 0;
  double nexty = 0;
  for (int i=0;i<N;i++) {
    if (x2[N-i-1] > cutx && y2[N-i-1] > cuty) {
      nextx = x2[N-i-1];
      nexty = y2[N-i-1];
      i = N;
    }
  }

  cout << "(firstx, firsty) = (" << firstx << ", " << firsty << ")" << endl;
  cout << "(lastx, lasty) = (" << lastx << ", " << lasty << ")" << endl;
  cout << "(nextx, nexty) = (" << nextx << ", " << nexty << ")" << endl;


  // Make expected band reach axes where needed
  // Find the closest frame edge to the end of the first contour
  int nearestedge1 = 0; // left
  double dist = fabs(lastx-1-xlow);
  if(fabs(lasty-yhigh) < dist) { // top
    dist = fabs(lasty-yhigh);
    nearestedge1 = 1;
  }
  if(fabs(lastx-1-xhigh) < dist) { // right
    dist = fabs(lastx-1-xhigh);
    nearestedge1 = 2;
  }
  if(fabs(lasty-ylow) < dist) { // bottom
    dist = fabs(lasty-ylow);
    nearestedge1 = 3;
  }

  // Find the closest frame edge to the end of the second contour
  int nearestedge2 = 0; // left
  double dist = fabs(nextx-1-xlow);
  if(fabs(nexty-yhigh) < dist) { // top
    dist = fabs(nexty-yhigh);
    nearestedge2 = 1;
  }
  if(fabs(nextx-1-xhigh) < dist) { // right
    dist = fabs(nextx-1-xhigh);
    nearestedge2 = 2;
  }
  if(fabs(nexty-ylow) < dist) { // bottom
    dist = fabs(nexty-ylow);
    nearestedge2 = 3;
  }

  if(nearestedge2 == nearestedge1) {
  	// when graphs will be connected on the same frame edge
  	// add two points just outside the boundary
    switch(nearestedge1) {
    case 0:
      grshade->SetPoint(point,xlow-100,lasty);
      point++;
      grshade->SetPoint(point,xlow-100,nexty);
      point++;
      break;
    case 1:
      grshade->SetPoint(point,lastx,yhigh+100);
      point++;
      grshade->SetPoint(point,nextx,yhigh+100);
      point++;
      break;
    case 2:
      grshade->SetPoint(point,xhigh+100,lasty);
      point++;
      grshade->SetPoint(point,xhigh+100,nexty);
      point++;
      break;
    case 3:
      grshade->SetPoint(point,lastx,ylow-100);
      point++;
      grshade->SetPoint(point,nextx,ylow-100);
      point++;
      break;
    }
  } else if(nearestedge2 == (nearestedge1-1 >= 0 ? nearestedge1-1 : nearestedge1+3)) {
	// when graphs will be connected across a corner, usually a triangle will be left in
	// to fix, add three points, two outside the boundary, and one outside the corner.
    switch(nearestedge2) {
    case 0:
      grshade->SetPoint(point,lastx,yhigh+100);
      point++;
      grshade->SetPoint(point,xlow-100,yhigh+100);
      point++;
      grshade->SetPoint(point,xlow-100,nexty);
      point++;
      break;      
    case 1:
      grshade->SetPoint(point,xhigh+100,lasty);
      point++;
      grshade->SetPoint(point,xhigh+100,yhigh+100);
      point++;
      grshade->SetPoint(point,nextx,yhigh+100);
      point++;
      break;      
    case 2:
      grshade->SetPoint(point,lastx,ylow-100);
      point++;
      grshade->SetPoint(point,xhigh+100,ylow-100);
      point++;
      grshade->SetPoint(point,xhigh+100,nexty);
      point++;
      break;      
    case 3:
      grshade->SetPoint(point,xlow-100,lasty);
      point++;
      grshade->SetPoint(point,xlow-100,ylow-100);
      point++;
      grshade->SetPoint(point,nextx,ylow-100);
      point++;
      break;      
    }
  }

  // this is the last point drawn in the second graph
  double finalx = 0;
  double finaly = 0;
  for (int i=0;i<N;i++) {
    if (x2[N-i-1] > cutx && y2[N-i-1] > cuty) {
      grshade->SetPoint(point,x2[N-i-1],y2[N-i-1]);
      finalx = x2[N-i-1];
      finaly = y2[N-i-1];
      point++;
    }
  }

  cout << "(finalx, finaly) = (" << finalx << ", " << finaly << ")" << endl;

  // // repeat for the other end of the band
  // int nearestedge3 = 0;
  // double dist = fabs(finalx-1-xlow);
  // if(fabs(finaly-yhigh) < dist) {
  //   dist = fabs(finaly-yhigh);
  //   nearestedge3 = 1;
  // }
  // if(fabs(finalx-1-xhigh) < dist) {
  //   dist = fabs(finalx-1-xhigh);
  //   nearestedge3 = 2;
  // }
  // if(fabs(finaly-ylow) < dist) {
  //   dist = fabs(finaly-ylow);
  //   nearestedge3 = 3;
  // }

  // int nearestedge4 = 0;
  // double dist = fabs(firstx-1-xlow);
  // if(fabs(firsty-yhigh) < dist) {
  //   dist = fabs(firsty-yhigh);
  //   nearestedge4 = 1;
  // }
  // if(fabs(firstx-1-xhigh) < dist) {
  //   dist = fabs(firstx-1-xhigh);
  //   nearestedge4 = 2;
  // }
  // if(fabs(firsty-ylow) < dist) {
  //   dist = fabs(firstx-ylow);
  //   nearestedge4 = 3;
  // }

  // if(nearestedge4 == nearestedge3) {
  //   switch(nearestedge3) {
  //   case 0:
  //     grshade->SetPoint(point,xlow-100,finaly);
  //     point++;
  //     grshade->SetPoint(point,xlow-100,firsty);
  //     point++;
  //     break;
  //   case 1:
  //     grshade->SetPoint(point,finalx,yhigh+100);
  //     point++;
  //     grshade->SetPoint(point,firstx,yhigh+100);
  //     point++;
  //     break;
  //   case 2:
  //     grshade->SetPoint(point,xhigh+100,finaly);
  //     point++;
  //     grshade->SetPoint(point,xhigh+100,firsty);
  //     point++;
  //     break;
  //   case 3:
  //     grshade->SetPoint(point,finalx,ylow-100);
  //     point++;
  //     grshade->SetPoint(point,firstx,ylow-100);
  //     point++;
  //     break;
  //   }
  // } else if(nearestedge4 == (nearestedge3-1 >= 0 ? nearestedge3-1 : nearestedge3+3)) {
  //   switch(nearestedge4) {
  //   case 0:
  //     grshade->SetPoint(point,finalx,yhigh+100);
  //     point++;
  //     grshade->SetPoint(point,xlow-100,yhigh+100);
  //     point++;
  //     grshade->SetPoint(point,xlow-100,firsty);
  //     point++;
  //     break;      
  //   case 1:
  //     grshade->SetPoint(point,xhigh+100,finaly);
  //     point++;
  //     grshade->SetPoint(point,xhigh+100,yhigh+100);
  //     point++;
  //     grshade->SetPoint(point,firstx,yhigh+100);
  //     point++;
  //     break;      
  //   case 2:
  //     grshade->SetPoint(point,finalx,ylow-100);
  //     point++;
  //     grshade->SetPoint(point,xhigh+100,ylow-100);
  //     point++;
  //     grshade->SetPoint(point,xhigh+100,firsty);
  //     point++;
  //     break;      
  //   case 3:
  //     grshade->SetPoint(point,xlow-100,finaly);
  //     point++;
  //     grshade->SetPoint(point,xlow-100,ylow-100);
  //     point++;
  //     grshade->SetPoint(point,firstx,ylow-100);
  //     point++;
  //     break;      
  //   }
  // }

  grshade->SetPoint(point++,firstx,firsty);

  grshade->Set(point);

  // Now draw the plot...
  grshade->SetFillStyle(fillStyle);
  grshade->SetFillColor(fillColor);
  //  grshade->SetMarkerStyle(21);
  grshade->Draw("F");
  
  return grshade;
}

void combine_and_plot_SUSYcurves_wino()
{
  //gROOT->LoadMacro("AtlasStyle.C");
  //SetAtlasStyle();

  Double_t contourLevel[1];
  contourLevel[0] = 1.0;
  
  TCanvas *c1 = new TCanvas();
  //  c1->SetGridx();
  //  c1->SetGridy();

  Int_t c_myYellow   = TColor::GetColor("#ffe938"); // TColor::GetColor( "#fee000" )
  Int_t c_myRed      = TColor::GetColor("#aa000");

  TLegend *leg = new TLegend(0.55,0.75,0.9,0.9);
  leg->SetFillColor(0);
  leg->SetBorderSize(0);

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

  TH2F *hObsNoTheoryUncertsXsecNominal = upperLimit->Clone("hObsNoTheoryUncertsXsecNominal");
  hObsNoTheoryUncertsXsecNominal->SetLineStyle(1);
  hObsNoTheoryUncertsXsecNominal->SetLineWidth(4);
  hObsNoTheoryUncertsXsecNominal->SetLineColor(c_myRed);
  hObsNoTheoryUncertsXsecNominal->SetContour(1, contourLevel);
  hObsNoTheoryUncertsXsecNominal->GetXaxis()->SetTitle("wino mass [GeV]");
  hObsNoTheoryUncertsXsecNominal->GetYaxis()->SetTitle("gluino mass [GeV]");

  TFile *fileNoTheoryUncertsXsecPlus1Sigma = new TFile("LepPhoton_NoTheoryUncertsXsecPlus1Sigma_AnalysisOutput_upperlimit__1_harvest_list.root");
  TH2F *hObsNoTheoryUncertsXsecPlus1Sigma = upperLimit->Clone("hObsNoTheoryUncertsXsecPlus1Sigma");
  hObsNoTheoryUncertsXsecPlus1Sigma->SetLineStyle(2);
  hObsNoTheoryUncertsXsecPlus1Sigma->SetLineWidth(2);
  hObsNoTheoryUncertsXsecPlus1Sigma->SetLineColor(c_myRed);
  hObsNoTheoryUncertsXsecPlus1Sigma->SetContour(1, contourLevel);

  TFile *fileNoTheoryUncertsXsecMinus1Sigma = new TFile("LepPhoton_NoTheoryUncertsXsecMinus1Sigma_AnalysisOutput_upperlimit__1_harvest_list.root");
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


  cout << "Now working on Obs +1sigma curve" << endl;
  hObsNoTheoryUncertsXsecPlus1Sigma->Draw("cont list");
  c1->Update();
  TObjArray *conts = (TObjArray*)gROOT->GetListOfSpecials()->FindObject("contours");
  vector<TGraph*> obsp1Curves = contoursToGraphs(conts, c_myRed, 2, 3);
  cout << "Found " << obsp1Curves.size() << " curves" << endl;

  cout << "Now working on Obs -1sigma curve" << endl;
  hObsNoTheoryUncertsXsecMinus1Sigma->Draw("cont list");
  c1->Update();
  TObjArray *conts = (TObjArray*)gROOT->GetListOfSpecials()->FindObject("contours");
  vector<TGraph*> obsm1Curves = contoursToGraphs(conts, c_myRed, 2, 3);
  cout << "Found " << obsm1Curves.size() << " curves" << endl;

  cout << "Now working on expected nominal curve" << endl;
  hExpNoTheoryUncertsXsecNominal->Draw("cont list");
  c1->Update();
  TObjArray *conts = (TObjArray*)gROOT->GetListOfSpecials()->FindObject("contours");
  vector<TGraph*> expCurves = contoursToGraphs(conts, kBlack, 2, 2);
  cout << "Found " << expCurves.size() << " curves" << endl;

  cout << "Now working on exp +1sigma curve" << endl;
  hExpPlus1NoTheoryUncertsXsecNominal->Draw("cont list");
  c1->Update();
  TObjArray *conts = (TObjArray*)gROOT->GetListOfSpecials()->FindObject("contours");
  vector<TGraph*> expp1Curves = contoursToGraphs(conts, c_myYellow, 2, 2);
  cout << "Found " << expp1Curves.size() << " curves" << endl;

  cout << "Now working on exp -1sigma curve" << endl;
  hExpMinus1NoTheoryUncertsXsecNominal->Draw("cont list");
  c1->Update();
  TObjArray *conts = (TObjArray*)gROOT->GetListOfSpecials()->FindObject("contours");
  vector<TGraph*> expm1Curves = contoursToGraphs(conts, c_myYellow, 2, 2);


  TH2F *hFrame = new TH2F("frame", "frame;wino mass [GeV];gluino mass [GeV]", 100, 100, 800, 100, 500, 1500);
  hFrame->Draw();

  newexpp1Curve = MergeTwoContours(expp1Curves[1], expp1Curves[0]);
  newCurve2 = FixContour(expp1Curves[2]);
  newAxisCurve = MakeNewContour(newCurve2);

  newexpp1Curve->SetLineColor(c_myYellow);
  expm1Curves[0]->SetLineColor(c_myYellow);

  //newexpp1Curve->Draw();
  //expp1Curves[2]->Draw();



  TGraph* grShadeExp = (TGraph*) DrawExpectedBand( newexpp1Curve, expm1Curves[0], c_myYellow, 1001,
  						   100, 700, 500, 1500)->Clone();

  grShadeExp->SetLineColor(c_myYellow);
  grShadeExp->SetLineWidth(0);

  TGraph* grShadeExp2 = (TGraph*) DrawExpectedBand( newAxisCurve, newCurve2, c_myYellow, 1001,
  						   100, 700, 500, 1500)->Clone();

  grShadeExp2->SetLineColor(c_myYellow);
  grShadeExp2->SetLineWidth(0);
  
  //grShadeExp->Draw();

  obsCurves[0]->Draw();
  obsp1Curves[0]->Draw();
  obsm1Curves[0]->Draw();

  expCurves[0]->Draw();

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
  l.DrawLatex(0.55,0.60,"ATLAS Preliminary");
  l.SetTextFont(42);
  l.DrawLatex(0.55,0.48,"#int Ldt = 4.7-4.8 fb^{-1}");
  l.DrawLatex(0.55,0.38,"#sqrt{s}=7 TeV");
  l.DrawLatex(0.2,0.96,"GGM: wino-like NLSP");
  l.DrawLatex(0.75,0.2,"#tilde{g} NLSP");

  l.SetTextSize(0.035);
  l.DrawLatex(0.64,0.70,"All limits at 95% CL");

  hFrame->Draw("axis,same");
}

