#!/usr/bin/env python

# the above command is the initiation code 'shbang'
# comments are important
# don't mix cases
# no spaces in the beginning of the code
# learn to assign variables.

#DNASeq = raw_input("enter DNA sequence:")
DNASeq = 'atgcaattggccaaatttgggccc'
DNASeq = DNASeq.upper()
# .upper() changes cases

print ( 'Sequence ' + DNASeq)
#print command displays the output
SeqLength = float( len( DNASeq ))

#use float command to add decimals

# str combines a 'string' with a non-string

print ( ' Length is ' + str (SeqLength ))

NumberA = DNASeq.count('A')
NumberT = DNASeq.count('T')
NumberG = DNASeq.count('G')
NumberC = DNASeq.count('C')

# using .count() command. 
# every function () needs parentheses() to work
 


print ('A: {:.2f}'.format(NumberA / SeqLength))
print ('T: {:.2f}'.format(NumberT / SeqLength))
print ('G: {:.2f}'.format(NumberG / SeqLength))
print ('C: {:.2f}'.format(NumberC / SeqLength))

TotalStrong = NumberG + NumberC
TotalWeak = NumberA + NumberT

if SeqLength <= 14:
	MeltTemp = ( 4 * TotalStrong ) + (2 * TotalWeak )
	
else:
	MeltTemp = 64.9 + 41 * (TotalStrong - 16.4) / SeqLength

print ( 'Melting Temp: {}'.format(MeltTemp) )

print ('Done')