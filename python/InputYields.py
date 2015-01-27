#!/usr/bin/env python

class Yields:
    '''A class to parse the input from a file and return a dictionry'''

    def __init__(self, filename):
        self.dict={}
        with open(filename, 'r') as f:
            for line in f:
                entries = line.split()
                if len(entries) >= 5:
                    if entries[0] not in self.dict:
                        self.dict[entries[0]] = {}
                    sub = self.dict[entries[0]]
                    if entries[1] not in sub:
                        sub[entries[1]] = {}
                    sub1 = sub[entries[1]]
                    if entries[2] not in sub1:
                        sub1[entries[2]] = entries[3:]
                    else:
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
        return float(self.dict[lepton][region][sample][2])/float(self.dict[lepton][region][sample][0])
    def GetJESDown(self, lepton, region, sample):
        return float(self.dict[lepton][region][sample][3])/float(self.dict[lepton][region][sample][0])
    def GetJER(self, lepton, region, sample):
        return float(self.dict[lepton][region][sample][4])/float(self.dict[lepton][region][sample][0])
    def GetPileUp(self, lepton, region, sample):
        return float(self.dict[lepton][region][sample][5])/float(self.dict[lepton][region][sample][0])
    def GetPileDown(self, lepton, region, sample):
        return float(self.dict[lepton][region][sample][6])/float(self.dict[lepton][region][sample][0])
        
