#!/usr/bin/python3

address1 = "http://cov-spectrum.org/explore/World/AllSamples/"
MonthChoose = ["Past2M/","Past6M/"]
address2 = "variant?nextcladePangoLineage="
ListChoose = ["JN.1.4.3*","LB.1*"]
aaMutationLabel = "&aaMutations1=S%3A"
aaMutation = ["S31-","S31F","S31P","F59S","F59L","S60P","T572I","T573I","K478R","A475V","A475S","S680F","S680P","S704L"]
baseline = "KP.2*"
address3 = "&nextcladePangoLineage1="
address4 = "&analysisMode=CompareToBaseline&&analysisMode=CompareToBaseline&</br></tr>"
final_address = ""
for month in MonthChoose:
    for variant in ListChoose:
        for mutation in aaMutation:
            current_address = address1 + month + address2 + baseline + aaMutationLabel + mutation + address3 + variant + address4
            final_address += current_address

print(final_address)
