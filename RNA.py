"""
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.
Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.
"""

def dna_transcriber(input_file):
    with open('output.txt','w') as output, open(input_file) as input:
        dna_string = input.readline()
        rna_string = dna_string.replace("T", "U")

          #Convert int to string
        output.write(rna_string) #Write transcribed string in to file





dna_transcriber('input.txt') #input file name is 'input.txt'
