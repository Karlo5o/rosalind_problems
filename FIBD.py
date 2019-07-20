"""
Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, which followed the recurrence relation Fn=Fn−1+Fn−2 and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male, one female) each subsequent month.
Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).
Given: Positive integers n≤100 and m≤20.
Return: The total number of pairs of rabbits that will remain after the n -th month if all rabbits live for m months.
"""

def mortal_fibonacci(input_file):
    with open('output.txt','w') as output, open(input_file) as input:
        parameters = input.read().split()
        n = int(parameters[0])
        m = int(parameters[1])
        table = [1,1]
        for i in range(2,m):
            table.append(table[i-1] + table[i-2])
        for j in range(m,n):
            table.append(sum(table[j-m:j-1]))
        print(table[-1])

mortal_fibonacci('input.txt')
