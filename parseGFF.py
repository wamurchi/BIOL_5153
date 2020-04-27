import argparse
import csv
import re
from Bio import SeqIO
from collections import defaultdict


def get_args():
	# create an argument parser object
	parser = argparse.ArgumentParser(description = "This script parses a GFF file and does stuff with it")

	# add positional arguments
	parser.add_argument("gff",   help="name of the GFF file")
	parser.add_argument("fasta", help="name of the FASTA file")

	# parse the arguments
	return parser.parse_args()


def parse_fasta():
	# read and parse the FASTA file
	return SeqIO.read(args.fasta, 'fasta')


def parse_gff(genome):
	# read GFF file, line by line
	with open(args.gff, 'r') as gff_file:
		
		# create a csv reader object
		reader = csv.reader(gff_file, delimiter="\t")

		for line in reader:
			# skip blank lines
			if not line:
				continue

			else:
				feature_type = line[2]
				start        = int(line[3])
				end          = int(line[4])
				strand       = line[6]
				attributes   = line[8]

				# test whether this is a CDS feature
				# if it is a CDS feature, then extract the substring/sequence
				if feature_type == 'CDS':
					string = attributes.split(' ')
					name = string[1]
					print(name)

					# extract this feature from the genome
					feature_seq = genome[start-1:end]
					match = re.search('Gene\s+(S+)\s+', attributes)
					gene_name = (match.group(1))

					#extract the gene name
					re.complie("Gene\s+(\S+)\s+")
					print(attributes)
					print(feature_seq)
					feature_GC = gc(feature_seq)
					GCround = round(feature_GC, 2)
					print (GCround)
					print ("{0:.2f}".format (feature_GC))

					if strand == '_':
						reverse = sequence.reserse_complement()
						print (reverse)
def gc(sequence):
	# calculate and print the GC content for that substring (2 decimal places)
	count_of_G = sequence.count('G')
	count_of_C = sequence.count('C')

	return(count_of_G + count_of_C)/len(sequence)


def main():
	genome_sequence = parse_fasta()
	parse_gff(genome_sequence.seq)


# get the command-line arguments before calling main()
args = get_args()

# execute the program by calling main
if __name__ == "__main__":
	main()


