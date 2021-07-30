#!bin/python
#script to manage alignment for selection analysis
#usage - python alignment_hack.py file1.txt file2.txt

from Bio import SeqIO
import sys

original_file = sys.argv[1]
extended_file = sys.argv[2]

with open(original_file) as original, open(extended_file, 'w') as extended:
    records = SeqIO.parse(original_file, 'fasta')
    for record in records:
        if len(record.seq)%3 == 1:
            record.seq = record.seq + "--"
        elif len(record.seq)%3 == 2:
            record.seq = record.seq + "-"
        SeqIO.write(record, extended, 'fasta')
