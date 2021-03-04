#This is the code for the solution of a codewar kata in python 
#Linear Regression of X and Y(6 kyu)

def regressionLine(x, y):
    SumSquareX = sum([n ** 2 for n in x])
    SumSquareY = sum([n ** 2 for n in y])
    SumX = sum(x)
    SumY = sum(y)
    SumXY = sum([x * y for x,y in zip(x,y)])
    a = ((SumSquareX*SumY) - (SumX*SumXY)) / float(((len(x) * SumSquareX) - SumX**2))
    b = ((len(x)*SumXY) - (SumX*SumY)) / float(((len(x)*SumSquareX) - SumX**2))
    a = round(a,4)
    b = round(b,4)
    return a,b