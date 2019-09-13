#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-

import argparse

CLI = argparse.ArgumentParser(prog='gc_content', usage='%(prog)s [options]',
                              description='calculate G C nucleotide %')

CLI.add_argument(
    '-i',
    type=str,
    default='GGG',
    help='string with no spaces'
)

ARGS = CLI.parse_args()

seq = ARGS.i

def gc_content(seq):
	split = []
	counts = []
	for base in seq:
		split.append(base)
	dna = ['A','C','T','G']
	for nucleotide in dna:
		counts.append(split.count(nucleotide))
	total = (float(counts[1])+float(counts[3]))/float(len(seq))*100
	print total
	
gc_content(seq)