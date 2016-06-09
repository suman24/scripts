#!/usr/bin/env python

InFileName = "reads100.fa"

InFile = open( InFileName, 'r' )

LineNumber = 0

OutFileName = "reads100.txt"

OutFile = open(OutFileName, 'w' )

import random

for Line in InFile:

	seq1 = ['AATTGGCC', 'TTAAGGCC', 'GGCCTTAA', 'CCGGAATT']

	nucl = ['A', 'T', 'G', 'C']



	if Line [ 0 ] in nucl:
		print (random.choice(seq1)) + Line


	else:
		print Line

	


InFile.close()







