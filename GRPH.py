"""
A graph whose nodes have all been labeled can be represented by an adjacency list, in which each row of the list contains the two node labels corresponding to a unique edge.
A directed graph (or digraph) is a graph containing directed edges, each of which has an orientation. That is, a directed edge is represented by an arrow instead of a line segment; the starting and ending nodes of an edge form its tail and head, respectively. The directed edge with tail v
and head w is represented by (v,w) (but not by (w,v)). A directed loop is a directed edge of the form (v,v).
For a collection of strings and a positive integer k, the overlap graph for the strings is a directed graph Ok in which each string is represented by a node, and string s is connected to string t with a directed edge when there is a length k suffix of s that matches a length k prefix of t, as long as s≠t; we demand s≠t
to prevent directed loops in the overlap graph (although directed cycles may be present).
Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
Return: The adjacency list corresponding to O3. You may return edges in any order.
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



def overlap_graph(input_file):
    with open('output.txt', 'w') as output:
        seqs = fasta_read(input_file)
        
        for id1, seq1 in seqs.items():
            for id2, seq2 in seqs.items():
                if id1 != id2:
                    if seq1[-3:] == seq2[:3]:
                        output.write(id1 + ' ' + id2 + '\n')



overlap_graph('input.txt')
