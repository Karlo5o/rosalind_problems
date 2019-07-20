"""
To allow for the presence of its varying forms, a protein motif is represented by a shorthand as follows: [XY] means "either X or Y" and {X} means "any amino acid except X." For example, the N-glycosylation motif is written as N{P}[ST]{P}.
You can see the complete description and features of a particular protein by its access ID "uniprot_id" in the UniProt database, by inserting the ID number into http://www.uniprot.org/uniprot/uniprot_id
Alternatively, you can obtain a protein sequence in FASTA format by following http://www.uniprot.org/uniprot/uniprot_id.fasta
For example, the data for protein B5ZC00 can be found at http://www.uniprot.org/uniprot/B5ZC00.
Given: At most 15 UniProt Protein Database access IDs.
Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.
"""

import requests, re
from FASTA import fasta_read


def find_glycosylation(input_file):
    with open('output.txt', 'w') as output, open(input_file) as input, open('test_out.txt', 'wb') as test_out:
        ids = input.read().split('\n')
        for id in ids:
            url = 'http://www.uniprot.org/uniprot/{}.fasta'.format(id)

            fasta = requests.get(url, allow_redirects=True).text
            fasta = fasta.split('\n')
            seq = "".join(fasta[1:])
            #print(id)
            if id == 'B6J655':
                print(seq[229:233])
            #print(seq)
            position = re.search("N[^P][ST][^P]", seq)
            start = 0
            id_written = False
            while position != None:
                if id == 'B6J655':
                    print(start)
                    print(position.group())
                if not id_written:
                    id_written = True
                    #print("{}\n".format(id))
                    output.write("{}\n".format(id))
                start = position.start() + start + 1
                #print("{} ".format(start))
                output.write("{} ".format(start))
                position = re.search("N[^P][ST][^P]", seq[start:])
            if id_written:
                output.write('\n')



# url = "https://www.uniprot.org/uniprot/P07204.fasta"
# fasta = requests.get(url, allow_redirects=True)
# open('download_test.fasta', 'wb').write(fasta.content)
find_glycosylation('input.txt')
