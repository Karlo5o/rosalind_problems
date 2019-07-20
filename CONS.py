"""
A matrix is a rectangular table of values divided into rows and columns. An m×n matrix has m rows and n columns. Given a matrix A, we write Ai,j to indicate the value found at the intersection of row i and column j.
Say that we have a collection of DNA strings, all having the same length n. Their profile matrix is a 4×n matrix P in which P1,j represents the number of times that 'A' occurs in the jth position of one of the strings, P2, j represents the number of times that C occurs in the j th position, and so on.
A consensus string c is a string of length n formed from our collection by taking the most common symbol at each position; the jth symbol of c therefore corresponds to the symbol having the maximum value in the j-th column of the profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)
"""

def fasta_read(input_file):
    "Process fasta file and return dictionary in the form ID:SEQ"
    with open(input_file) as input:
        result = {}
        seq = ""
        id = ""
        for line in input.readlines():
            if line[0] == '>': #if the start with '>'
                if seq: #dealing with previous sequence
                    result[id] = seq
                    seq = "" #ready for new sequence
                id = line.lstrip('>').rstrip()

            else:
                seq += line.rstrip()
        result[id] = seq #adding last sequence
    return result

def print_result(cons_string, profile, output):
    output.write(cons_string + '\n')
    for nucleotide in ['A', 'C', 'G', 'T']:
        output.write(nucleotide + ':' + ' ')
        output.write(" ".join(profile[nucleotide]) + '\n')


def find_consensus(input_file):
    with open('output.txt', 'w') as output:
        seqs = list(fasta_read(input_file).values())
        print(seqs)
        profile = {"A": [], 'C': [], 'G': [], 'T': []}
        cons_seq = ""
        for i in range(len(seqs[0])):
            A_number, C_number, G_number, T_number = [0,0,0,0]
            for j in range(len(seqs)):
                if seqs[j][i] == 'A': A_number += 1
                elif seqs[j][i] == 'T': T_number += 1
                elif seqs[j][i] == 'C': C_number += 1
                else: G_number += 1
            max_value = max([A_number, C_number,G_number,T_number])
            if A_number == max_value: cons_seq += "A"
            elif C_number == max_value: cons_seq += "C"
            elif G_number == max_value: cons_seq += "G"
            else: cons_seq += "T"
            profile['A'].append(str(A_number))
            profile['C'].append(str(C_number))
            profile['G'].append(str(G_number))
            profile['T'].append(str(T_number))
        print_result(cons_seq, profile, output)

find_consensus('input.txt')
