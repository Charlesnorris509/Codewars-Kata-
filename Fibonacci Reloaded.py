# This is the code for the solution of a codewars kata in python
# Fibonacci Reloaded 6kyu the 27/02/2021 

def fib(n):
    temp = [0, 1]
    for i in range(n -1):
        temp[0], temp[1] = temp[1], sum(temp)
    return temp[0]