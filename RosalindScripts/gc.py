import itertools
from Bio import SeqIO

with open("/Users/kivanccorut/Desktop/sci_computing/rosalind_problems/RosalindScripts/rosalind_gc.txt", "rU") as handle:
    
    for record in SeqIO.parse(handle, "fasta"):
        totalcount = len(record.seq)
        count=0
        for i in record.seq:
            if i == 'C':
                count +=1
            elif i == 'G':
                count +=1
        gc = count/totalcount*100
        print(record.id,"\n",gc)
handle.close()