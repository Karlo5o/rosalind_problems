"""
A common substring of a collection of strings is a substring of every member of the collection. We say that a common substring is a longest common substring if there does not exist a longer common substring. For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".
Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".
Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
"""

from FASTA import fasta_read

def common_motif(input_file):
    with open('output.txt', 'w') as output:
        seqs = list(fasta_read(input_file).values())
        i = 0 #start index
        j = 1 #end index
        longest_motif = ""

        while i < len(seqs[0]) and j < len(seqs[0]):
            current_motif = seqs[0][i:j]
            flag = True
            for seq in seqs[1:]:
                if current_motif not in seq:
                    flag = False
            if flag:
                if len(current_motif) > len(longest_motif):
                    longest_motif = current_motif
                    j += 1
            else:
                i += 1
                j = i + len(longest_motif) + 1
        output.write(longest_motif)


common_motif('input.txt')
