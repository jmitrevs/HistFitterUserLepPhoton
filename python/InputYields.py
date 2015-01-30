#!/usr/bin/env python
from math import sqrt

class Yields:
    '''A class to parse the input from a file and return a dictionry'''

    def __init__(self, filename, mergeWCR=False):
        self.dict={}
        with open(filename, 'r') as f:
            for line in f:
                entries = line.split()
                if len(entries) >= 5:
                    alt = False
                    lepton = entries[0]
                    if mergeWCR and entries[1].startswith("WCR"):
                        alt = True
                        lepton = 'El'
                    if lepton not in self.dict:
                        self.dict[lepton] = {}
                    sub = self.dict[lepton]
                    if entries[1] not in sub:
                        sub[entries[1]] = {}
                    sub1 = sub[entries[1]]
                    if entries[2] not in sub1:
                        sub1[entries[2]] = entries[3:]
                    else:
                        if alt:
                            #then add entries
                            valOrig = sub1[entries[2]]
                            valAdd = entries[3:]
                            valOrig[0] = float(valOrig[0]) + float(valAdd[0])
                            for i in range(1, len(valAdd)):
                                valOrig[i] = sqrt(float(valOrig[i])**2+float(valAdd[i])**2)
                        else:
                            print "Duplicate",entries
                            raise ValueError("Have a duplicate entry in the input file")
        #print self.dict

    def GetYield(self, lepton, region, sample):
        #print "GetYield", lepton, region, sample
        yie = float(self.dict[lepton][region][sample][0])
        if yie < 0:
            return 0
        else:
            return yie

    def GetYieldUnc(self, lepton, region, sample):
        #print "GetYieldUnc", lepton, region, sample
        return float(self.dict[lepton][region][sample][1])

                        
    def GetJESUp(self, lepton, region, sample):
        yd = float(self.dict[lepton][region][sample][0])
        if yd != 0: 
            return float(self.dict[lepton][region][sample][2])/yd
        else:
            return yd

    def GetJESDown(self, lepton, region, sample):
        yd = float(self.dict[lepton][region][sample][0])
        if yd != 0: 
            return float(self.dict[lepton][region][sample][3])/yd
        else:
            return yd

    def GetJER(self, lepton, region, sample): 
        yd = float(self.dict[lepton][region][sample][0])
        if yd != 0: 
            return float(self.dict[lepton][region][sample][4])/yd
        else:
            return yd

    def GetPileUp(self, lepton, region, sample):
        yd = float(self.dict[lepton][region][sample][0])
        if yd != 0: 
            return float(self.dict[lepton][region][sample][5])/yd
        else:
            return yd

    def GetPileDown(self, lepton, region, sample):
        yd = float(self.dict[lepton][region][sample][0])
        if yd != 0: 
            return float(self.dict[lepton][region][sample][6])/yd
        else:
            return yd

    def GetTransFact(self, lepton, region, sample):
        yd = float(self.dict[lepton][region][sample][0])
        if yd != 0: 
            return float(self.dict[lepton][region][sample][7])/yd
        else:
            return yd

    def GetMatrixUp(self, lepton, region, sample):
        yd = float(self.dict[lepton][region][sample][0])
        if yd != 0: 
            return float(self.dict[lepton][region][sample][8])/yd
        else:
            return yd

    def GetMatrixDown(self, lepton, region, sample):
        yd = float(self.dict[lepton][region][sample][0])
        if yd != 0: 
            return float(self.dict[lepton][region][sample][9])/yd
        else:
            return yd

        
