#!/usr/bin/env python3.7
#-*- coding: utf-8 -*


import numpy as np
import argparse

CLI = argparse.ArgumentParser(prog='scribnslate', usage='%(prog)s [options]',
                              description='transcribes and translates 3 RF')

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

def transcribe(seq):
	split = []
	for base in seq:
		split.append(base)
	for n, i in enumerate(split):
		if i is "T":
			split[n]="U"
	return "".join(split)

def split(rna,n):
    for i in range(n, len(rna), 3):
        yield rna[i:i + 3]

def translate(rna):


    seqsplit = []

    for i in range(0,3):
        seqsplit.append(list(split(rna,i)))

    seqsplit = np.asarray(seqsplit)

    for orf in range(0,3):

        codons = []
        brotein = []

        for codon in seqsplit[orf]:
            codons.append("".join(codon))


        for i in codons:
            for codon in table:
                if i == codon[0:3]:
                    brotein.append(codon[3])
        proteinseq = "".join(brotein)
        print("ORF+"+str(orf)+":     "+proteinseq)

rna = transcribe(seq)

translate(rna)