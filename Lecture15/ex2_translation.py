#!usr/bin/python3


gencode = {
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
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}


def reverse_complement(dna):
    reverse_strand = ''
    d1, d2 = 'ACGTN', 'TGCAN'
    for i in reversed(dna):
        reverse_strand += d2[d1.index(i)]
    return reverse_strand


def translate_dna(dna, frame=1):
    dna = dna.upper() if frame > 0 else reverse_complement(dna.upper())
    frame = abs(frame)

    aa = ''
    for i in range(frame - 1, len(dna), 3):
        if len(dna[i:i + 3]) == 3:
            if dna[i:i + 3] in gencode:
                aa += gencode[dna[i:i + 3]]
            else:
                aa += 'X'
    return aa


assert translate_dna("ATGTTCGGT") == "MFG"
assert translate_dna("ATCGATCGATCGTTGCTTATCGATCAG") == "IDRSLLIDQ"
assert translate_dna("actgatcgtagctagctgacgtatcgtat") == "TDRS_LTYR"
assert translate_dna("ACGATCGATCGTNACGTACGATCGTACTCG") == "TIDRXVRSYS"
