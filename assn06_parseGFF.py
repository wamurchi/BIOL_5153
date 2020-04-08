#! /usr/bin/env python3

import argparse
import csv
from Bio import SeqIO

#create an agrument parser object 
parser = argparse.ArgumentParser(description = "This script parses a GFF file and does stuff with it")

# add postional arguments
parser.add_argument("gff",   help="name the GFF file")
parser.add_argument("fasta", help="name of the FASTA file")

#parse the argument
args = parser.parse_args()

# read and parse the FASTA file
genome = SeqIO.read(args.fasta, 'fasta')


# read GFF file, line by line
with open(args.gff, 'r') as gff_file:
	
	#create a csv reader object
	reader = csv.reader(gff_file, delimiter="\t")

	for line in reader:
		if not line:
			continue

		else: 
			column = line [2]
			start = line[3]
			end = line [4]
			print(column, start, end)

		# if it is a CDS feature, then extract the substring/sequence
	reader = csv.reader(gff_file, delimiter="\t")

	for line in reader:
		if line [2] =="CDS"
			print(line[2])

			#if (start =="CDS"):
			#print(start, end)

# calcuate and print the GC content for that substring (2 decimal places)
dna_percent = open(args.fasta)
dna_contents = dna_percent.read()
base = (dna_contents)
# Ignore case sensitivity
'GC' == 'gc'
# count bases
length = len(dna_contents)
GC_count = base.count('CG')
GC_content = (GC_count / length, round(c,2))
# now print the counts
print("GC %: " + str(GC_content))
			
# or wirte a function to calcuate GC content:
dna_percent = open(args.fasta)
dna_contents = dna_percent.read()

def get_at_content():
 length = len(dna_contents)
 g_count = dna_contents.upper().count('A')
 c_count = dna_contents.upper().count('T')
 at_content = (g_count + c_count) / length
 return round(gc_content, 2) 

print(get_at_content())


#args.fasta.close() 
#args.gff.close()
