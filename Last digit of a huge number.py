#This is the code for a codewars kata solution
# @CharlesNorris 6/03/21
# The last digit in a huge number python (3kyu)

def last_digit(lst):
    ret = 1
    for i in reversed(lst):
        ret = i **(ret if ret < 4 else ret % 4 + 4)
    return ret % 10
