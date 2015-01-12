#! /usr/bin/env python

'''This module contains the yields
'''

from __future__ import division
import math

ELECTRON = 0
MUON = 1

#indexed by electron/muon
CRs=[]
VR1s=[]
VR2s=[]
SRs=[]

#Electron channel yields: CR
CRs.append({
            "regions": ("WCR"                 ,"WCRbtag"               ,"WCRbveto"),               
            "Wgamma" : (302.344 , 3.001 , 41.305 , 1.272 , 270.249 , 2.834 ),
            "Wjets" : (15.517 , 1.953  , 10.453 , 1.305 , 8.214 , 1.224   ),
            "ttbargamma" : (35.669 , 0.825  , 42.880 , 1.098 , 6.456 , 0.348   ),
            "ttbarDilep" : (11.168 , 0.424  , 12.829 , 0.543 , 2.150 , 0.184   ),
            "singletop" : (12.728 , 0.257  , 12.780 , 0.307 , 3.498 , 0.129   ),
            "diboson" : (0.981 , 0.151   , 0.001 , 0.001  , 0.977 , 0.153   ),
            "Zgamma" : (10.309 , 0.414  , 1.658 , 0.214  , 9.046 , 0.382   ),
            "Zjets" : (1.224 , 0.087   , 0.131 , 0.022  , 1.120 , 0.088   ),
            "gammajets" : (43.302 , 0.275  , 5.367 , 0.102  , 37.935 , 0.255  ),
            "diphotons" : (23.756 , 2.187  , 4.424 , 0.922  , 20.287 , 2.081  ),

            "data" : (477.000 , 0             , 76.000      ,0       , 401.000 , 0)   }  )

#Muon channel yields: CR
CRs.append({
            "regions": ("WCR" ,"WCRbtag"               ,"WCRbveto"           ),
            "Wgamma" : (344.825 , 3.187 , 49.322 , 1.375  , 306.589 , 3.003 ),
            "Wjets" : (22.063 , 1.953  , 13.700 , 1.305  , 12.398 , 1.224  ),
            "ttbargamma" : (41.743 , 0.894  , 49.988 , 1.185  , 7.623 , 0.381   ),
            "ttbarDilep" : (11.776 , 0.433  , 13.529 , 0.559  , 2.400 , 0.195   ),
            "singletop" : (14.159 , 0.265  , 13.809 , 0.308  , 4.059 , 0.141   ),
            "diboson" : (1.685 , 0.187   , 0.136 , 0.068   , 1.578 , 0.180   ),
            "Zgamma" : (20.397 , 0.602  , 2.757 , 0.254   , 18.282 , 0.570  ),
            "Zjets" : (4.446 , 0.339   , 0.108 , 0.022   , 4.351 , 0.358   ),
            "gammajets" : (12.815 , 0.342  , 2.044 , 0.141   , 10.771 , 0.311  ),

            "data" : (476.000  ,0           , 78.000    ,0          , 398.000    ,0         ) } )
 
 
 


#Electron channel yields: VR1
VR1s.append({            
            "regions": ("HMET"              ,"HMEThHT"               ,"HMETmeff"                ),
            "Wgamma" : (155.009 , 2.133  , 85.722 , 1.582 , 10.542 , 0.560 ),
            "Wjets" : (12.128 , 1.341   , 6.933 , 0.911  , 0.571 , 0.098  ),
            "ttbargamma" : (22.083 , 0.650   , 3.513 , 0.258  , 2.294 , 0.209  ),
            "ttbarDilep" : (5.883 , 0.307    , 1.929 , 0.177  , 0.268 , 0.065  ),
            "singletop" : (5.702 , 0.173    , 1.762 , 0.107  , 0.708 , 0.061  ),
            "diboson" : (0.999 , 0.160    , 0.339 , 0.082  , 0.145 , 0.073  ),
            "Zgamma" : (1.974 , 0.195    , 1.206 , 0.157  , 0.103 , 0.036  ),
            "Zjets" : (0.131 , 0.022    , 0.000 , 0.000  , 0.005 , 0.001  ),
            "gammajets" : (0.883 , 0.108    , 0.210 , 0.076  , 0.246 , 0.026  ),
            "diphotons" : (0.325 , 0.325    , 0.000 , 0.000  , 0.325 , 0.325  ),

            "data" : (181.000  ,0            , 92.000   ,0          , 7.000     ,0         )})
  

            
# Muon channel yields: VR1

VR1s.append({            
          "regions": ("HMET"              ,"HMEThHT"               ,"HMETmeff"                ),
          "Wgamma" : (164.154 , 2.179 , 90.239 , 1.621       , 10.409 , 0.549 ),
          "Wjets" : (14.663 , 1.341  , 8.935 , 0.911        , 0.405 , 0.098  ),
          "ttbargamma" : (22.484 , 0.652  , 3.160 , 0.244        , 2.314 , 0.207  ),
          "ttbarDilep" : (6.206 , 0.318   , 1.973 , 0.179        , 0.315 , 0.072  ),
          "singletop" : (6.049 , 0.179   , 1.631 , 0.106        , 0.690 , 0.063  ),
          "diboson" : (0.787 , 0.124   , 0.497 , 0.104        , 0.050 , 0.029  ),
          "Zgamma" : (5.821 , 0.327   , 4.672 , 0.298        , 0.242 , 0.077  ),
          "Zjets" : (0.117 , 0.022   , 0.102 , 0.039        , 0.001 , 0.000  ),
          "gammajets" : (9.434 , 0.238   , 2.594 , 0.158        , 2.228 , 0.074  ),

          "data" : (214.000 , 0            , 104.000, 0                 , 12.000   , 0          )})
            

# Electron channel yields: VR2

VR2s.append({            
            "regions": ("HMT"              ,"HMThHT"               ,"HMTmeff"                ),
            "Wgamma" : (65.486 , 1.321 , 37.457 , 0.990   , 2.491 , 0.266 ),
            "Wjets" : (8.917 , 0.756  , 2.979 , 0.332    , 0.232 , 0.050 ),
            "ttbargamma" : (10.078 , 0.438 , 1.688 , 0.180    , 0.365 , 0.080 ),
            "ttbarDilep" : (7.487 , 0.347  , 1.919 , 0.177    , 0.120 , 0.045 ),
            "singletop" : (2.645 , 0.128  , 0.665 , 0.074    , 0.315 , 0.049 ),
            "diboson" : (0.867 , 0.143  , 0.648 , 0.127    , 0.000 , 0.000 ),
            "Zgamma" : (23.454 , 0.625 , 16.373 , 0.522   , 1.395 , 0.167 ),
            "Zjets" : (1.551 , 0.090  , 1.079 , 0.111    , 0.041 , 0.004 ),
            "gammajets" : (25.915 , 0.223 , 20.068 , 0.187   , 0.739 , 0.045 ),
            "diphotons" : (19.815 , 1.943 , 11.721 , 1.489   , 0.827 , 0.413 ),

            "data" : (163.000, 0            , 81.000, 0               , 13.000 , 0           )})
 
 
#Muon channel yields: VR2

VR2s.append({            
            "regions": ("HMT"              ,"HMThHT"               ,"HMTmeff"                ),
            "Wgamma" : (79.467 , 1.465    , 46.264 , 1.114 , 2.663 , 0.266 ),
            "Wjets" : (7.736 , 0.756     , 2.674 , 0.332  , 0.160 , 0.050 ),
            "ttbargamma" : (10.961 , 0.458    , 1.997 , 0.199  , 0.332 , 0.076 ),
            "ttbarDilep" : (7.232 , 0.341     , 1.884 , 0.174  , 0.092 , 0.037 ),
            "singletop" : (2.967 , 0.130     , 0.591 , 0.067  , 0.219 , 0.035 ),
            "diboson" : (1.008 , 0.125     , 0.674 , 0.103  , 0.071 , 0.071 ),
            "Zgamma" : (37.440 , 0.809    , 28.240 , 0.702 , 1.471 , 0.159 ),
            "Zjets" : (0.790 , 0.063     , 0.627 , 0.072  , 0.017 , 0.003 ),
            "gammajets" : (-0.419 , 0.159    , 0.681 , 0.131  , -0.105 , 0.028),

            "data" : (129.000, 0             , 83.000, 0             , 4.000, 0             )})
            
#Electron channel yields: SR
            
SRs.append({
            "regions": ("SRS","SRW"        ),
            "Wgamma" : (0.572 , 0.128  , 6.717 , 0.436  ),
            "Wjets" : (0.374 , 0.080  , 0.875 , 0.204    ),
            "ttbargamma" : (0.238 , 0.066  , 1.353 , 0.162 ),
            "ttbarDilep" : (0.254 , 0.066  , 0.354 , 0.077 ),
            "singletop" : (0.127 , 0.037  , 0.144 , 0.033 ),
            "diboson" : (0.021 , 0.015  , 0.305 , 0.079 ),
            "Zgamma" : (0.000 , 0.000  , 0.016 , 0.008 ),
            "Zjets" : (0.005 , 0.002  , 0.008 , 0.004 ),
            "gammajets" : (0.000 , 0.143 , 0.000 , 0.143   ),
            "diphotons" : (0.002 , 0.002  , 0.000 , 0.000 ),
            "data" : (1.588, 0    , 9.771, 0    )})

# Muon channel yields: SR

SRs.append({
            "regions": ("SRS","SRW"       ),
            "Wgamma" : (0.525 , 0.117, 8.908 , 0.513   ),
            "Wjets" : (0.234 , 0.080, 0.860 , 0.204     ),
            "ttbargamma" : (0.371 , 0.085, 1.665 , 0.181   ),
            "ttbarDilep" : (0.248 , 0.060, 0.317 , 0.071    ),
            "singletop" : (0.095 , 0.029, 0.208 , 0.036   ),
            "diboson" : (0.028 , 0.014, 0.368 , 0.092   ),
            "Zgamma" : (0.147 , 0.055, 1.174 , 0.150   ),
            "Zjets" : (0.006 , 0.002, 0.002 , 0.001    ),
            "gammajets" : (0.000 , 0.613, 0.000 , 0.613    ),
            
            "data" : (1.653 , 0, 13.502, 0       )})



def GetYield(lepton, region, sample):
    if lepton == 'El':
        lep = ELECTRON
    else:
        lep = MUON

    if region == "WCRbtag":
        return CRs[lep][sample][2]
    elif region == "WCRbveto":
        return CRs[lep][sample][4]
        
    elif region == "HMEThHT":
        return VR1s[lep][sample][2]
    elif region == "HMETmeff":
        return VR1s[lep][sample][4]

    elif region == "HMThHT":
        return VR2s[lep][sample][2]
    elif region == "HMTmeff":
        return VR2s[lep][sample][4]

    elif region == "SRS":
        return SRs[lep][sample][0]
    elif region == "SRW":
        return SRs[lep][sample][2]

def GetYieldUnc(lepton, region, sample):

    if sample == "data":
        return math.sqrt(GetYield(lepton, region, sample))

    if lepton == 'El':
        lep = ELECTRON
    else:
        lep = MUON

    if region == "WCRbtag":
        return CRs[lep][sample][3]
    elif region == "WCRbveto":
        return CRs[lep][sample][5]
        
    elif region == "HMEThHT":
        return VR1s[lep][sample][3]
    elif region == "HMETmeff":
        return VR1s[lep][sample][5]

    elif region == "HMThHT":
        return VR2s[lep][sample][3]
    elif region == "HMTmeff":
        return VR2s[lep][sample][5]

    elif region == "SRS":
        return SRs[lep][sample][1]
    elif region == "SRW":
        return SRs[lep][sample][3]


