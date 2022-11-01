#!usr/bin/python3


dna = "ATGCATCATG"
k = 2	# kmer size
n = 2	# more than this number found


all_kmers = {}

for i in range(len(dna) - k + 1):	
	kmer = dna[i:i+k]
	all_kmers[kmer] = all_kmers.get(kmer, 0) + 1

for key in all_kmers:
	if all_kmers[key] > n:
		print(key)

