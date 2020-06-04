#!/usr/bin/env python3.7
#-*- coding: utf-8 -*-

import argparse
import numpy as np

CLI = argparse.ArgumentParser(prog='proteinMW', usage='%(prog)s [options]',
                              description='calculates molecular weight (MW) based on input aa seq')

CLI.add_argument(
    '-i',
    type=str,
    default='HELP',
    help='string with no spaces'
)

ARGS = CLI.parse_args()

seq = ARGS.i

mwtable = np.asarray([
("A", 71.03711),
("C", 103.00919),
("D", 115.02694),
("E", 129.04259),
("F", 147.06841),
("G", 57.02146),
("H", 137.05891),
("I", 113.08406),
("K", 128.09496),
("L", 113.08406),
("M", 131.04049),
("N", 114.04293),
("P", 97.05276),
("Q", 128.05858),
("R", 156.10111),
("S", 87.03203),
("T", 101.04768),
("V", 99.06841),
("W", 186.07931),
("Y", 163.06333)])

seqsplit = list(seq)

mwlist = []

def proteinMW(seq):
    for aa in seqsplit:
        for value in range(0,len(mwtable)):
            if aa == mwtable[value,0]:
                mwlist.append(float(mwtable[value,1]))
    mw = np.sum(mwlist)

    print("MW (Da):")
    print(int(mw))

proteinMW(seq)
