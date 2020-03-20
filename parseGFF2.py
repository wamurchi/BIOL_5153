#! /usr/bin/env python3
# defining the input infile

input = open("watermelon.gff", "r")
watermelonGenes = []
for line in input:
    line = line.rstrip("\n")
    line = line.split("\t")
    line = line[8].split(" ")
    if(line[1] == "similar"):
        print("similar")
    if(line[1] == "inverted"):
        print("inverted")
    else:
        if line[1] in watermelonGenes:
            print("already found")
        else:
            watermelonGenes.append(line[1])
        watermelonGenes.sort()
        print(watermelonGenes)
