from Bio.Seq import Seq 


def read_dna(file):
	
	#read sequence
	with open(file, "r") as f:
		seq = Seq(f.read().replace("\n", "").upper())

	return seq
	
