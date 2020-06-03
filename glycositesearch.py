#!/usr/bin/env python3.7
#-*- coding: utf-8 -*-

import argparse
import wget
import re

CLI = argparse.ArgumentParser(prog='glycositesearch', usage='%(prog)s [options]',
                              description='Find N-linked glyco sites, input FASTA code NOT seq')

CLI.add_argument(
    '-i',
    type=str,
    default='B5ZC00',
    help='string with no spaces'
)

ARGS = CLI.parse_args()

id = ARGS.i

def glycositesearch(id):

    prot_id = id
    url = "http://www.uniprot.org/uniprot/"
    link = url + prot_id + ".fasta"
    file = wget.download(link)

    dat = open(file, 'r')
    line_num = 0
    start = False

    seq = []
    for line in dat:
            if (re.search('>',line)):
                start=True
                continue
            if(start):
                seq.append(line[0:].strip())

    seq = ''.join(str(elem) for elem in seq)
    seq = list(seq)
    index = []
    for aa in range(0,len(seq)):
        if seq[aa] == 'N' and seq[aa+1] != 'P' and seq[aa+3] != 'P' and aa <= len(seq)-4:
            if seq[aa+2] == 'S' or seq[aa+2] == 'T':
                index.append(aa)

    if len(index) !=0:
    	print('	Glyco sites:	', index[:])
    else:
        print("No N-glyco sites found")

glycositesearch(id)