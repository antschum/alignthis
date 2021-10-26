from Bio import Align
import alignthis.alignme as am

s1 = am.read_dna('dnafile_1.txt')
s2 = am.read_dna('dnafile_2.txt')

aligner = Align.PairwiseAligner()
aligner.match_score = 2
aligner.mode = 'local'

alignments = aligner.align(s1, s2)

#print alignments
for a in alignments:
	print(a)


