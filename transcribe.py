#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-

import argparse

CLI = argparse.ArgumentParser(prog='gc_content', usage='%(prog)s [options]',
                              description='transcribe DNA>RNA')

CLI.add_argument(
    '-i',
    type=str,
    default='GGG',
    help='string with no spaces'
)

ARGS = CLI.parse_args()

seq = ARGS.i

def transcribe(seq):
	split = []
	for base in seq:
		split.append(base)
	for n, i in enumerate(split):
		if i is "T":
			split[n]="U"
	print "".join(split)

transcribe(seq)
