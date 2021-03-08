#This is the solution for a codewars kata 
# @CharlesNorris 08/03/21
#Permutation in Python 
#Difficulty 4kyu

import itertools
def permutations(string):
    return sorted([''.join(p) for p in set(itertools.permutations(string,len(string)))])
