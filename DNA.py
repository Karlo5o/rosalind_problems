

def nucleotides_counter(input_file):
    with open('output.txt','w') as output, open(input_file) as input:
        dna_string = input.readline().upper()
        counter = {'A':0, 'T':0, 'G':0, 'C':0}

        for nucleotide in dna_string: counter[nucleotide] += 1

        output_string = " ".join([str(counter['A']), str(counter['C']), str(counter['G']), str(counter['T'])]) #Convert int to string
        output.write(output_string) #Write final string in to file





nucleotides_counter('input.txt') #input file name is 'input.txt'
