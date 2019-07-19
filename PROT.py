"""
The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet (all letters except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols. Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.
The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.
Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
Return: The protein string encoded by s.
"""

def protein_sequence(input_file):
    with open('output.txt','w') as output, open(input_file) as input:
        proteins = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
        codons = [a+b+c for a in "UCAG" for b in "UCAG" for c in "UCAG"]
        translator = dict(zip(codons,proteins))
        sequence = input.read().strip()
        protein = ""
        for i in range(0, len(sequence), 3):
            protein += translator[sequence[i:i+3]]
        output.write(protein.replace('*',''))


protein_sequence('input.txt')
