#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-

import argparse

CLI = argparse.ArgumentParser(prog='gc_content', usage='%(prog)s [options]',
                              description='reverse complement')

CLI.add_argument(
    '-a',
    type=str,
    default='GGG',
    help='string with no spaces'
)

ARGS = CLI.parse_args()

seq = ARGS.a

def complement(seq):
	split = []
	for base in seq:
		split.append(base)
	for n, i in enumerate(split):
		if i is "T":
			split[n]="A"
		if i is "A":
			split[n]="T"
		if i is "C":
			split[n]="G"
		if i is "G":
			split[n]="C"
	print  "".join(list(reversed(split)))
	
complement(seq)