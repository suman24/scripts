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

TotalStrong = 0
TotalWeak = 0

Bases = "CGTA"
for Base in Bases:
	Count = DNASeq.count(Base)
	Frequency = Count / SeqLength
	print (  '{}: {:.2f}'.format(Base, Frequency) )
	if Base in 'GC':
		TotalStrong = TotalStrong + Count
	else:
		TotalWeak = TotalWeak + Count



# using .count() command. 
# every function () needs parentheses() to work
 


if SeqLength <= 14:
	MeltTemp = ( 4 * TotalStrong ) + (2 * TotalWeak )
	
else:
	MeltTemp = 64.9 + 41 * (TotalStrong - 16.4) / SeqLength

print ( 'Melting Temp: {}'.format(MeltTemp) )

print ('Done')