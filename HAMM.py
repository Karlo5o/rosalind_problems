"""
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.
Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t).
"""

def hamming_distance(input_file):
    with open('output.txt','w') as output, open(input_file) as input:
        seqs = input.read().split('\n')
        
        dist = 0
        for nuc1, nuc2 in zip(seqs[0], seqs[1]):
            if nuc1 != nuc2:
                dist += 1
        output.write(str(dist))

hamming_distance('input.txt')
