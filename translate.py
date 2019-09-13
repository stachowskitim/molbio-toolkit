#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-

import argparse

CLI = argparse.ArgumentParser(prog='translate', usage='%(prog)s [options]',
                              description='translate into amino acid sequence')

CLI.add_argument(
    '-i',
    type=str,
    default='GGG',
    help='string with no spaces'
)

ARGS = CLI.parse_args()

seq = ARGS.i

table = ['UUUF','CUUL','AUUI','GUUV',
'UUCF','CUCL','AUCI','GUCV',
'UUAL','CUAL','AUAI','GUAV',
'UUGL','CUGL','AUGM','GUGV',
'UCUS','CCUP','ACUT','GCUA',
'UCCS','CCCP','ACCT','GCCA',
'UCAS','CCAP','ACAT','GCAA',
'UCGS','CCGP','ACGT','GCGA',
'UAUY','CAUH','AAUN','GAUD',
'UACY','CACH','AACN','GACD',
'UAA*','CAAQ','AAAK','GAAE',
'UAG*','CAGQ','AAGK','GAGE',
'UGUC','CGUR','AGUS','GGUG',
'UGCC','CGCR','AGCS','GGCG',
'UGA*','CGAR','AGAR','GGAG',
'UGGW','CGGR','AGGR','GGGG']

def split(seq):
	for i in range(0,len(seq),3):
		yield seq[i:i+3]

def translate(seq,table):
	codons = []
	brotein = []
	x = list(split(seq))
	for codon in x:
		codons.append("".join(codon))
	for i in codons:
		for codon in table:
			if i == codon[0:3]:
				brotein.append(codon[3])
	print "".join(brotein)

translate(seq, table)