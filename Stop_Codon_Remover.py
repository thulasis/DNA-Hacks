#!/bin/python

from Bio.Seq import Seq
from Bio import SeqIO


import sys
"Usage: python Stop_Codon_Remover.py file.fasta > outfile.fasta"

stop_codons = ["TAG", "TGA", "TAA"]
fasta_file = SeqIO.parse(open(sys.argv[1]), 'fasta')
for fasta in fasta_file:
    ID, sequence = fasta.description, str(fasta.seq)
    try:
        assert(len(sequence)% 3 == 0)
    except:
        raise IOError("sequence is not divisible of three".format(ID))
    print(">{}".format(ID))    
    print ("".join([sequence[i:i+3] for i in range(0, len(sequence) -3 +1, 3) if sequence[i:i+3] not in stop_codons]))