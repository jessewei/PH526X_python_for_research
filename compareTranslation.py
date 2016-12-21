## HarvardX PH526X Week 3 Video 3.1.4
## Translating the DNA Sequence

def readSeq(filename="dna.txt"):
    """
    Reads and returns the input sequence with special
    characters ('\n','\r') removed.
    """
    # Importing the DNA sequence
    with open(filename, 'r') as f:
        seq = f.read()
    # Cleaning the DNA sequence
    seq = seq.replace("\n", '') # replacing new lines
    seq = seq.replace("\r", '') # replacing backslashes
    return seq

# Procedure:
# Step 1: Check that the length of the sequence is divisible by 3
# Step 2: Look up each 3-letter string in the table and store the result
# Step 3: Continue until the end of the sequence

def translateDNA(seq):
    """
    Translate a string containing a nucleotide sequence
    into a string containing the corresponding sequence
    of amino acides. Nucleotides are translated in tri-
    plets using the table dictionary; each amino acid is
    encoded with a string of length 1.
    """
    # DNA Translation Dictionary
    table = {
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
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    
    protein = ""
    if len(seq) % 3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i:i + 3]
            protein += table[codon]
    else:
        print("Sequence length not divisible by 3")
    return protein

if __name__ == "__main__":
    dna = readSeq("dna.txt")
    prt = readSeq("protein.txt")
    # according to NCBI: take dna[20:938]
    print("DNA sequence is the same as protein sequence?", end=' ')
    # since the last character is '_' in dna, should exclude it
    print(prt == translateDNA(dna[20:938])[:-1])
