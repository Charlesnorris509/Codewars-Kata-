"""This is the code for the solution of the roman numerals decoder 
level 6kyu in Codewars"""

def solution(roman):
    symbols = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    values = [symbols[i] for i in roman]
    for i in range(len(values)- 1):
        if values[i] < values[i + 1]:
            values[i] *= -1
    return sum(values)

solution('MCV')
