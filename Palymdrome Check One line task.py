#This is the code for the solution of a codewars kata in python 
#Difficulty = 3 kyu
#One Line Task: Palindrome String

palindrome=lambda n,s:(s*n)[:n//2]+(s*n)[~-n//2::-1]


