#!/usr/bin/python3
​
address1="http://cov-spectrum.org/explore/World/AllSamples/"
MonthChoose=["Past2M/","Past6M/"]
address2="variant?nextcladePangoLineage="
ListChoose=["JN.1.4.3*","LB.1*"]
aaMutationLabel="&aaMutations1=S%3A"
aaMutation=["S31-","S31F","S31P","F59S","F59L","S60P","T572I","T573I","K478R","A475V","A475S","S680F","S680P","S704L"]
address3="&nextcladePangoLineage1="
baseline = "KP.2*"
address4="&analysisMode=CompareToBaseline&&analysisMode=CompareToBaseline&"
address5=address1+MonthChoose[0]
address6=address2+ListChoose[0]
address7=aaMutationLabel+aaMutation[0]
print (address5+address6+address7)
print (15)
print (34)
​
