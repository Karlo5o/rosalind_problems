"""
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word;
the length of a string is the number of symbols that it contains.
An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."
Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s
.
"""

def nucleotides_counter(input_file):
    with open('output.txt','w') as output, open(input_file) as input:
        dna_string = input.readline().upper()
        counter = {'A':0, 'T':0, 'G':0, 'C':0}

        for nucleotide in dna_string: counter[nucleotide] += 1

        output_string = " ".join([str(counter['A']), str(counter['C']), str(counter['G']), str(counter['T'])]) #Convert int to string
        output.write(output_string) #Write final string in to file





nucleotides_counter('input.txt') #input file name is 'input.txt'
