 
'assn01-1' 
find *nad* -print

'assn01-2'
top
Processes: 328 total, 2 running, 326 sleeping, 1157 threads                                                                               15:31:46
Load Avg: 1.04, 1.24, 1.31  CPU usage: 1.21% user, 1.21% sys, 97.56% idle   SharedLibs: 304M resident, 64M data, 51M linkedit.
MemRegions: 40130 total, 2216M resident, 181M private, 1344M shared. PhysMem: 5764M used (1182M wired), 2427M unused.
VM: 1800G vsize, 1370M framework vsize, 0(0) swapins, 0(0) swapouts. Networks: packets: 2673210/389M in, 53916/9148K out.
Disks: 324261/5418M read, 131537/2907M written.

PID    COMMAND      %CPU TIME     #TH   #WQ  #PORT MEM    PURG   CMPR PGRP  PPID STATE    BOOSTS          %CPU_ME %CPU_OTHRS UID       FAULTS
10258  top          2.2  00:02.33 1/1   0    25    3824K  0B     0B   10258 9576 running  *0[1]           0.00000 0.00000    0         24225+
10257  Google Chrom 0.0  00:00.07 12    1    98    13M    0B     0B   9334  9334 sleeping *0[5]           0.00000 0.00000    409898556 9073
10250  Google Chrom 0.0  00:00.92 13    1    150   40M    0B     0B   9334  9334 sleeping *0[7]           0.00000 0.00000    409898556 24591
10238  CoreServices 0.0  00:00.07 3     1    147   3516K  0B     0B   10238 1    sleeping *0[1]           0.00000 0.00000    409898556 4554
10237  com.apple.sp 0.0  00:00.25 2     1    48    15M    0B     0B   10237 1    sleeping *0[1]           0.00000 0.00000    409898556 7482
10236  com.apple.au 0.0  00:00.01 2     2    17    844K   0B     0B   10236 1    sleeping  0[2]           0.00000 0.00000    409898556 2592
10235  backupd      0.0  00:00.03 2     1    43    1660K  0B     0B   10235 1    sleeping *0[1]           0.00000 0.00000    0         8046
10234  AudioCompone 0.0  00:00.09 2     1    59    3780K  32K    0B   10234 1    sleeping  0[1]           0.00000 0.00000    409898556 3691
10233  Google Chrom 0.0  00:00.54 7     1    126   11M    0B     0B   9334  9334 sleeping *0[5]           0.00000 0.00000    409898556 8272
10139  mdworker_sha 0.0  00:00.30 4     1    65    7700K  0B     0B   10139 1    sleeping *0[1]           0.00000 0.00000    409898556 25927
10136  mdworker_sha 0.0  00:00.35 4     1    61    8268K  0B     0B   10136 1    sleeping *0[1]           0.00000 0.00000    409898556 30114
10135  mdworker_sha 0.0  00:00.18 4     1    61    6260K  0B     0B   10135 1    sleeping *0[1]           0.00000 0.00000    409898556 17526
10134  mdworker_sha 0.0  00:00.03 3     1    56    2988K  0B     0B   10134 1    sleeping *0[1]           0.00000 0.00000    409898556 4760

'assn01-3'
grep 'misc_feature' watermelon.gff > IR_regions.gff | cut -f 4-6 IR_regions.gff | sort -k4 -r 

'assn01-4'
grep -cv IR IR_regions.gff; grep -c IR IR_regions.gff
34
3
#more chloroplast fragments come from outside the IR regions 

'assn01-5'
grep -o 'GGATCC' *.fasta* > BamHI_genes
less BamHI_genes
grep -o 'ATT' *.fasta*
#After comparing the output, all of the BamHI sites also have EcoRI sites.

'assn01-6'
head -n 1000 shaver_etal.csv | tail -n 500 

'assn01-7'
sort -k2,2 -r -k3,2 fruit.txt | column -t 
