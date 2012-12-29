#!/usr/bin/env python

__author__ = "Sean Gibbons"
__copyright__ = "Copyright 2012, BPHS"
__credits__ = ["Sean Gibbons", "James Crooks"]
__license__ = "GPL"
__version__ = "0.0.0-dev"
__maintainer__ = "Sean Gibbons"
__email__ = "monsieursean@gmail.com"
__status__ = "Development"

##Usage: python PDB_parser.py <input PDB file name>

import fileinput, re

pdb = []

#make pdb variable a list, with each line from the pdb file as an element (new-line removed)

for line in fileinput.input():
    line = line.rstrip()
    pdb.append(line)

seq = []

#pull out the sequence info, with each line an element in a list

for line in pdb:
  if line.startswith('SEQRES'):
		line.split()
		seq.append(line[19:])

#join the list into a string, with space delimeters between the triplet aa letter codes

seq_cat = ' '.join(seq)

#create dictionary for aa triplet and single-letter codes

aa_dict = {'ALA': 'A', 'ARG':'R','ASN':'N','ASP':'D','CYS':'C','GLU':'E','GLN':'Q','GLY':'G','HIS':'H','ILE':'I','LEU':'L','LYS':'K','MET':'M','PHE':'F','PRO':'P','SER':'S','THR':'T','TRP':'W','TYR':'Y','VAL':'V'}

#stole this from the web - use library to convert triple-letter aa codes to single-letter code string

pattern = re.compile(r'\b(' + '|'.join(aa_dict.keys()) + r')\b')
seq_single = pattern.sub(lambda x: aa_dict[x.group()], seq_cat)



atom = []
atom_seq = []

for line in pdb:
	if line.startswith('N ',13,15):
		line = line.rstrip()
		line.split()
		atom_seq.append(line[17:20])

atom_seq_cat = ' '.join(atom_seq)

pattern = re.compile(r'\b(' + '|'.join(aa_dict.keys()) + r')\b')
xray_seq_single = pattern.sub(lambda x: aa_dict[x.group()], atom_seq_cat)

print '\n'
print 'SEQRES a.a. sequence: '
print seq_single
print '\n'
print 'X-Ray a.a. sequence: '
print xray_seq_single
print '\n'
if seq_single == xray_seq_single:
	print "SEQRES sequence and X-Ray sequence show 100% match!\n"
else:
	print "SEQRES sequence and X-Ray sequence do not match!/n"


	



