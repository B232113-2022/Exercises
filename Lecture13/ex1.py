#!usr/bin/python3

data_file = './data.csv'

genes_file = open(data_file, 'r')


q1, q2, q3, q4, q5 = [], [], [], [], []

for line in genes_file:
	sp_name, seq, gene_name, exp_level = line.split(',')
	AT_content = (seq.count('a') + seq.count('t')) / len(seq)

	if sp_name in ['Drosophila melanogaster', 'Drosophila simulans']:
		q1.append(gene_name)
	
	if 90 <= len(seq) <= 110:
		q2.append(gene_name)

	if AT_content < 0.5 and int(exp_level) > 200:
		q3.append(gene_name)

	if sp_name != 'Drosophila melanogaster' and (gene_name[0] in 'kh'):
		q4.append(gene_name)

	gene_AT = 'high' if AT_content > 0.65 else 'low' if AT_content < 0.45 else 'medium'
	q5.append((gene_name, gene_AT))

print('Q1: Genes from the species ~melanogaster or ~simulans are:\n', q1, '\n')
print('Q2: Genes with base length of 90-110 are:\n', q2, '\n')
print('Q3: Genes with AT content < 0.5, expression level > 200 are:\n', q3, '\n')
print('Q4: Gene names starting with k or h except for those from ~melanogaster are:\n', q4, '\n')
print('Q5: Gene names and its AT content:\n', q5, '\n')

genes_file.close()
