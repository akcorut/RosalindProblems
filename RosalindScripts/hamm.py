lineList = [line.rstrip('\n') for line in open("/Users/kivanccorut/Desktop/sci_computing/rosalind_problems/RosalindScripts/rosalind_hamm.txt")]
seq1, seq2 = map(str, zip(lineList))

def noMatch(seq1, seq2):
    mismatches = []
    mismatchCount = 0
    for i in range (len(seq1)):
        if seq1[i] != seq2[i]:
            mismatchCount += 1
            mismatches.append('|')
        else:
            mismatches.append(' ')
    print(seq1)
    print("".join(mismatches))
    print(seq2)
    print(mismatchCount)

noMatch(seq1, seq2)

