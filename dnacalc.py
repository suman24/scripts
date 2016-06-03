#!/usr/bin/env python

# comments are important
# don't mix cases

DNASeq = 'ATGAAC'

print ( 'Sequence ' + DNASeq )

SeqLength = float( len( DNASeq ))

# str combines a 'string' with a non-string

print ( ' Length is ' + str (SeqLength ))

NumberA = DNASeq.count('A')
NumberT = DNASeq.count('T')
NumberG = DNASeq.count('G')
NumberC = DNASeq.count('C')

print('A: ' + str(NumberA / SeqLength))