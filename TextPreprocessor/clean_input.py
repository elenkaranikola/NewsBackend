# coding: utf-8
import sys
sys.path.insert(1, '/Users/elenikaranikola/Desktop/NewsBackend')
from utilities import finalNormalizeFullPath

my_input = sys.argv[1]

final = finalNormalizeFullPath(my_input)

res = ""
for x in final:
    res = res + " " + x
print(" ")
print("RESULTS!!!")
print(" ")
print(res)