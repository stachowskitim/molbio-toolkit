#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-

import argparse

CLI = argparse.ArgumentParser(prog='motif_count', usage='%(prog)s [options]',
                              description='returns positions where a substring occurs')

CLI.add_argument(
    '-a',
    type=str,
    default='GGG',
    help='string with no spaces'
)

CLI.add_argument(
    '-b',
    type=str,
    default='GGG',
    help='string with no spaces'
)

ARGS = CLI.parse_args()

seq = ARGS.a
sub = ARGS.b


def motif_count(seq,sub):
	list = []
	for i in range(len(seq)):
		if sub == seq[i:i+len(sub)]:
			list.append(i+1)
	print list
	
motif_count(seq,sub)