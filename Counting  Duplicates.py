#This is the solution for a codewar kata in python
#Counting Duplicates (6 Kyu)


def duplicate_count(text):
    count = 0
    text = text.lower()
    for char in set(text):
        if text.count(char) > 1:
            count = count + 1
    return count  
