#This is the solution of a codewars kata
#Difficulty : 6kyu
#Nova polynomial . multiply

# return the product of the two polynomials p1 and p2.  
def poly_multiply(p1, p2):
    res = [0] * (len(p1) + len(p2) -1)
    for x1, i1 in enumerate(p1):
        for x2, i2 in enumerate(p2):
            res[x1 + x2] += i1 * i2 
    if  res.count(0) == len(res):
        return []
    else:
        return res
