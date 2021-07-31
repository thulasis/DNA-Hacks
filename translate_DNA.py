#!/bin/python
#basic script to convert DNA to protein sequence
#"Usage: python translate_DNA.py file.fasta > outfile.fasta"

import sys

dna_file = sys.argv[1]
f = open(dna_file, "r")
seq = f.read()

#replace spaces or newlines in file

seq = seq.replace("\n","") #new lines
seq = seq.replace("\r", "") #carriages or hidden characters
seq = seq.upper()

def translate_DNA(seq):
    
    codon_table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                 
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
        'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
    }
    
    start_codon = seq.find('ATG')
    start_codon = seq.find('GTG')
    protein = ''
    i = start_codon
    while i < len(seq)-2:
        codon = seq[i:i+3]
        aa = codon_table[codon]
        if aa == '*':
            break
            print "Stop Codon Found!!!"
        i = i+3
        protein = protein + aa
    return protein
      
header = ''
seq = ''
for line in open(dna_file):
    if line[0] == '>':
        if header != '':
            print header
            translate_DNA(seq)

        header = line.strip()
        seq = ''
    else:
        seq =seq + line.strip()

print header

print translate_DNA(seq)