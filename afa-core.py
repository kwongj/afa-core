#!/usr/bin/env python3
# Script by JK

# Usage
import argparse
from argparse import RawTextHelpFormatter
import os
import sys
import re
from Bio import AlignIO

# Functions
# Log a message to stderr
def msg(*args, **kwargs):
	print(*args, file=sys.stderr, **kwargs)

# Log an error to stderr and quit with non-zero error code
def err(*args, **kwargs):
	msg(*args, **kwargs)
	sys.exit(1);

# Check file exists
def check_file(f):
	return os.path.isfile(f)

# Check if file is in FASTA format
def check_fasta(f):
	if not os.path.isfile(f) or os.path.getsize(f) < 1:
		return False
	with open(f, 'r') as fasta:
		if fasta.readline()[0] != '>':						# Check if header starts with ">"
			return False
		for line in fasta:
			line = line.strip()
			if not line or line[0] == '>':	
				continue
			if bool(re.search('[^ACTGactgNn\-]', line)):	# Check if there are non-nucleotide characters in sequence
				return False
	return True

parser = argparse.ArgumentParser(
	formatter_class=RawTextHelpFormatter,
	description='Generates lists of core/non-core sites from a multi-FASTA alignment for ClonalFrameML\n',
	usage='\n  %(prog)s [--out invariant.fa] FASTA')
parser.add_argument('fasta', metavar='FASTA', nargs=1, help='original multi-FASTA alignment file')
parser.add_argument('--pre', metavar='PREFIX', default='cfml', help='specify output prefix for files (default="cfml")')
parser.add_argument('--version', action='version', version='%(prog)s v0.1')
args = parser.parse_args()

core_out = args.pre + '.core-sites.txt'
noncore_out = args.pre + '.noncore-sites.txt'

# Check input/output files
if not check_file(args.fasta[0]):
	err('ERROR: Cannot find "{}". Check file exists in the specified directory.'.format(args.fasta[0]))
if not check_fasta(args.fasta[0]):
	err('ERROR: Check "{}" is in FASTA format.'.format(args.fasta[0]))
if args.pre:
	if check_file(core_out):
		err('ERROR: "{}" already exists.'.format(core_out))
	if check_file(noncore_out):
		err('ERROR: "{}" already exists.'.format(noncore_out))

# Check core/non-core sites
core = []
noncore = []
msg('Checking for core/non-core sites ... please wait'.format(args.fasta[0]))
aln = AlignIO.read(args.fasta[0], 'fasta')
for col in range(0, len(aln[0])):
	if bool(re.search('[^ACGT]', aln[:,col])):
		noncore.append(str(col+1))
	else:
		core.append(str(col+1))
with open(core_out, 'w') as f:
	f.write('\n'.join(core))
	msg('{} core sites written to {}.'.format(len(core), core_out))
with open(noncore_out, 'w') as f:
	f.write('\n'.join(noncore))
	msg('{} non-core sites written to {}.'.format(len(noncore), noncore_out))

sys.exit(0)
