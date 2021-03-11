#This is the solution for a codewars  kata in python
#Difficulty  : 5kyu
#Extract  the domain name from a URL

import re

def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')

