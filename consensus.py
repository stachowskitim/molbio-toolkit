#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-

import argparse

CLI = argparse.ArgumentParser(prog='consensus', usage='%(prog)s [options]',
                              description='finds most common seq from list of seqs')

CLI.add_argument(
    '-i',
    nargs='+',
    default=[],
    help='list of strings separated by spaces'
)

ARGS = CLI.parse_args()

seq = ARGS.i

def consensus(seq):
	dna = ['A','C','T','G']
	test = []
	conseq = []
	tseq = zip(*seq)
	for i in range(len(tseq)):
		counts = []
		for base in dna:
			counts.append(tseq[i].count(base))
		maxbasepos = counts.index(max(counts))
		conseq.append(dna[maxbasepos])
	print "".join(conseq)
	
consensus(seq)
