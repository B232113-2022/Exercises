#!usr/bin/python3


seq_list = ['ATTGTACGG', 'AATGAACCG', 'AATGAACCC', 'AATGGGAAT']


def identical_positions(dna1, dna2):
	count = 0
	for letter1, letter2 in zip(dna1, dna2):
		if letter1 == letter2:
			count += 1
	return count / len(dna1) * 100



for idx, seq1 in enumerate(seq_list):
	for seq2 in seq_list[idx + 1:]:
		print(seq1, seq2, f'{identical_positions(seq1, seq2):.2f}')

