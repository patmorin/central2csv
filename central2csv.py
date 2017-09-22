#!/usr/bin/python3
""" Convert Carleton Central's class lists into simple CSV files """
import os
import sys
import re


def first_student_number(lines):
    for i in range(len(lines)):
        if re.match(r'\d{9}$', lines[i]):
            return i
    return len(lines)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <infile>".format(sys.argv[0]))
        sys.exit(-1)
    infile = sys.argv[1]
    print("Reading from {}".format(infile))
    lines = open(infile).read().splitlines()
    lines = [ x for x in lines if re.search(r'X\d', x)]
    lines = [ x.split('"')[1] for x in lines]
    lines = lines[first_student_number(lines):]   # TODO: This could be more robust
    records = [ lines[5*i:5*(i+1)] for i in range(len(lines)//5)]
    records = [ ",".join([r[0], r[1], r[2], r[4]]) for r in records ]

    print("First record = '{}'".format(records[0]))
    print("Last record = '{}'".format(records[-1]))

    outfile = "{}.csv".format(os.path.splitext(infile)[0])
    print("Writing to {}".format(outfile))

    fp = open(outfile, 'w')
    for r in records:
        fp.write(r + '\n')
    fp.close()
