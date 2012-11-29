
## m['qcdwza'], m['sqrtnobsa'], m['qcdtta'], m['jersysa'], m['jessysa'], m['mcstatta'], m['scalewa'], m['btagsysa'], m['qcdsiga'], m['qcdfakea'], m['wsysa'], m['lersysa'], m['lessysa'], m['totbkgsysa'], m['scaleta'], m['topsysa'], m['mcstatwa']


def tablefragment(m,table,signalRegions,skiplist,chanStr,showPercent):
  tableline = ''

  tableline += '''
\\begin{table}
\\begin{center}
\\setlength{\\tabcolsep}{0.0pc}
\\begin{tabular*}{\\textwidth}{@{\\extracolsep{\\fill}}l'''

  for region in signalRegions:
    tableline += "c"   
    #print " region = ", region
  tableline += '''}
\\noalign{\\smallskip}\\hline\\noalign{\\smallskip}
{\\bf %s channel}                                   ''' % (table)

  for region in signalRegions:
    tableline += " & " + region + "           "   
#    tableline += " & " + region.replace("_meffInc","").replace("_metmeff2Jet","").replace("SR","").replace("SS","SL") + "           "   
   # print " region = ", region

  tableline += ''' \\\\
\\noalign{\\smallskip}\\hline\\noalign{\\smallskip}
%%'''

  tableline += '''
Total statistical $(\\sqrt{N_{\\rm obs}})$             '''
  for region in signalRegions:
    #for index, n in enumerate(m[region]['sqrtnobsa']):
    #print     "   region =", region
    #print " m[region]['sqrtnobsa'] = ", m[region]['sqrtnobsa']
    tableline += " & $\\pm " + str(("%.2f" %m[region]['sqrtnobsa'])) + "$       "
  tableline += '''\\\\
%%'''

  tableline += '''
Total background systematic              '''

  #for index, n in enumerate(m['totbkgsysa']):
  #  tableline += " & $\\pm " + str(("%.2f" %m['totbkgsysa'][index][3])) + "$       "
  for region in signalRegions:
    tableline += " & $\\pm " + str(("%.2f" %m[region]['totsyserr'])) + "$       "

  tableline += '''      \\\\
\\noalign{\\smallskip}\\hline\\noalign{\\smallskip}
\\noalign{\\smallskip}\\hline\\noalign{\\smallskip}
%%''' 


  doAsym=False
  # Assumption is that all regions have all the parameters, true for RooExpandedFitResult
  m_listofkeys = m[signalRegions[0]].keys()
  m_listofkeys.sort()
##   for region in signalRegions:
##     oneRegion = m[region]
##     m_listofkeys = oneRegion.keys()
##     m_listofkeys.sort()
  for name in m_listofkeys:
    # print "\n parameter = ", name, " printing"
    #  tableline = addlinetosystable(tableline,oneRegion,name,doAsym,skiplist)try:
    if name not in skiplist:
      printname = name
      printname = printname.replace('syserr_','')
      printname = printname.replace('_','\_')
      for index,region in enumerate(signalRegions):
        ##  try:
##           m[region].has_key(name)
##           #print " \n", name
##         except:
##           print " \n", name, "  not inside the systematics table"
##           break
##         #return tableline
        
        #   print " index = ",index

        # first line character
        if index == 0:
          #print " \n PRINT FIRST CHARACTER"
          tableline += "\n" + printname + "      "
          
        if not showPercent:
          tableline += "   & $\\pm " + str(("%.2f" %m[region][name])) + "$       "
        else:
          percentage = m[region][name]/m[region]['totsyserr'] * 100.0
          #     if percentage >10:
          #      tableline += "   & $\\pm " + str(("%.2f" %m[region][name])) + " [" + str(("%.1f" %percentage)) + "\\%] $       "
          if percentage <1:
            tableline += "   & $\\pm " + str(("%.2f" %m[region][name])) + " [" + str(("%.2f" %percentage)) + "\\%] $       "
          else:
            tableline += "   & $\\pm " + str(("%.2f" %m[region][name])) + " [" + str(("%.1f" %percentage)) + "\\%] $       "
                    
          
        if index == len(signalRegions)-1:
          #print " \n PRINT LAST CHARACTER"
          tableline += '''\\\\
%%'''

#  return tableline

##     doPrint=False
##    ##  if name.startswith("gamma") or name.startswith("alpha_QCDNorm"):
## ##       for sr in signalRegions:
## ##         if name.find(sr)>-1:
## ##           doPrint=True
##     if name.startswith("alpha") and name.endswith("se"):
##       for sr in signalRegions:
##         if sr.startswith("SSEl"):
##           doPrint=True
##     elif name.startswith("alpha") and name.endswith("el"):
##       for sr in signalRegions:
##         if sr.find("El")>-1 and not sr.startswith("SSEl"):
##           doPrint=True
##     elif name.startswith("alpha") and name.endswith("sm"):
##       for sr in signalRegions:
##         if sr.startswith("SSMu"):
##           doPrint=True
##     elif name.startswith("alpha") and name.endswith("mu"):
##       for sr in signalRegions:
##         if sr.find("Mu")>-1 and not sr.startswith("SSMu"):
##           doPrint=True
##     elif name.startswith("alpha") and name.endswith("ee"):
##       for sr in signalRegions:
##         if sr.find("ee")>-1:
##           doPrint=True
##     elif name.startswith("alpha") and name.endswith("em"):
##       for sr in signalRegions:
##         if sr.find("em")>-1:
##           doPrint=True
##     elif name.startswith("alpha") and name.endswith("mm"):
##       for sr in signalRegions:
##         if sr.find("mm")>-1:
##           doPrint=True
##     else:
##       doPrint=True
##     print "\n\n XXX par = ", name, " doPrint = ", doPrint
##     if doPrint:

  tableline += '''
\\noalign{\\smallskip}\\hline\\noalign{\\smallskip}
\\end{tabular*}
\\end{center}
\\caption[Breakdown of uncertainty on background estimates]{
Breakdown of the dominant systematic uncertainties on background estimates in the various signal regions.
Note that the individual uncertainties can be correlated, and do not necessarily add up quadratically to 
the total background uncertainty.
\\label{table.results.bkgestimate.uncertainties.%s}}
\\end{table}
%%''' % (chanStr) 
    
  return tableline


def givetuple(m,name):
  ntuple = ( m[name][0][1], m[name][0][3], m[name][1][1], m[name][1][3], m[name][2][1], m[name][2][3], m[name][3][1], m[name][3][3] )
  return ntuple

def givetuplesym(m,name):
  print name
  ntuple = ( m[name][0][3], m[name][1][3], m[name][2][3], m[name][3][3] )
  return ntuple

def addlinetosystable(tableline,oneRegion,name,doAsym,skiplist):
  try:
    oneRegion.has_key(name)
    print " \n", name
  except:
    print " \n", name, "  not inside the systematics table"
    return tableline

  if name not in skiplist:
  ##   if doAsym:
##       tableline += '\n'+ printname + '''   & ${}^{+%.2f}_{-%.2f}$ & ${}^{+%.2f}_{-%.2f}$  & ${}^{+%.2f}_{-%.2f}$ & ${}^{+%.2f}_{-%.2f}$ \\\\
##       %%''' % givetuple(m,name)
    printname = name
    printname = printname.replace('_','\_')
    #  tableline += "\n" + printname + ''' & $\\pm %.2f$ & $\\pm %.2f$  & $\\pm %.2f$ & $\\pm %.2f$ \\\\
    #    %%''' % givetuplesym(m,name)
    
    tableline += "\n" + printname
    # for index, n in enumerate(m[name]):
    #    tableline += "   & $\\pm " + str(("%.2f" %m[name][index][3])) + "$       "
    tableline += "   & $\\pm " + str(("%.2f" %oneRegion[name])) + "$       "
    tableline += '''\\\\
    %%'''

  return tableline
 
