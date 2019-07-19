"""
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s,
then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement sc of s.
"""

def reverse_complement(input_file):
    with open('output.txt','w') as output, open(input_file) as input:
        complement = {"A": "T", "C": "G", "T": "A", "G": "C"}
        dna_string = input.readline()
        reverse_string = reversed(dna_string)
        result = ""
        for nucleotide in reverse_string: result += complement[nucleotide]
        output.write(result) #Write final string in to file





reverse_complement('input.txt') #input file name is 'input.txt'
