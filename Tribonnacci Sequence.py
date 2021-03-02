#This is the code for the codewars solution kata
#Tribonacci Sequence (6 kyu) in python

def Tribonacci(signature, n):
    if n > 3:
        for i in range(3, n):
            signature.append(sum(signature[-3:]))
    return signature[:n]

