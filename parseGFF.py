#! /usr/bin/env python3
# defining the input infile
infile = "watermelon.gff"

# open and parse watermelon.gff, pull out column 7
with open(infile, 'r') as watermelon:
    watermelon_genes = []
    for line in watermelon:
        line = line.rstrip('\n')
        fields = line.split('\t')
        if (fields[7] =="Gene"):
            append.watermelon_genes()
            sort.watermelon_genes()
            print(watermelon_genes)
