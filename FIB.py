"""
A sequence is an ordered collection of objects (usually numbers), which are allowed to repeat. Sequences can be finite or infinite. Two examples are the finite sequence (π,−2–√,0,π) and the infinite sequence of odd numbers (1,3,5,7,9,…). We use the notation an to represent the n-th term of a sequence.
A recurrence relation is a way of defining the terms of a sequence with respect to the values of previous terms. In the case of Fibonacci's rabbits from the introduction, any given month will contain the rabbits that were alive the previous month, plus any new offspring.
A key observation is that the number of offspring in any month is equal to the number of rabbits that were alive two months prior. As a result, if Fn represents the number of rabbit pairs alive after the n-th month, then we obtain the Fibonacci sequence having terms Fn that are defined by the recurrence relation Fn=Fn−1+Fn−2 (with F1=F2=1 to initiate the sequence). Although the sequence bears Fibonacci's name, it was known to Indian mathematicians over two millennia ago.
When finding the n-th term of a sequence defined by a recurrence relation, we can simply use the recurrence relation to generate terms for progressively larger values of n.
This problem introduces us to the computational technique of dynamic programming, which successively builds up solutions by using the answers to smaller cases.
Given: Positive integers n≤40 and k≤5.
Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

UNIVERSAL PATTERN:
F(n) = F(n-1) + F(n-2) * k
"""

def fibonacci(input_file):
    with open('output.txt','w') as output, open(input_file) as input:
        parameters = input.readline().split()
        n = int(parameters[0])
        k = int(parameters[1])
        table = [1,1] #table for fast access to fibonacci values
        if n > 2:
            for j in range(2, n):
                table.append(table[j-1] + k * table[j-2])

        output.write(str(table[-1]))

fibonacci('input.txt')
