#This is the code for the solution of a Codewars kata 
#Detect Pangram(6 kyu) in python

import string

def is_pangram(s):
    set = []
    s = s.lower()
    for  i in s:
        if i.isalpha():
            if i not in set:
                set.append(i)
    return len(set) == 26