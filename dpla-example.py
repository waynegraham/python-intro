from dpla.api import DPLA

dpla = DPLA('ca5e8bd04608d564ee60e37f8556bf18')

result = dpla.search('cooking')

print result.items[0:3]

