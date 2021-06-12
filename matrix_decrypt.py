#!/bin/python3

import math
import os
import random
import re
import sys


# first_multiple_input = input().rstrip().split()

# n = int(first_multiple_input[0])

# m = int(first_multiple_input[1])
n = 7
m = 3


matrix = ['Tsi', 'h%x', 'i #', 'sM ', '$a ', '#t%', 'ir!']

# for _ in range(n):
#     matrix_item = input()
#     matrix.append(matrix_item)


decoded = ''
for j in range(m):
    for i in range(n):
        print(i, j)
        print(matrix[i][j])
        decoded += matrix[i][j]

# print(decoded)
pattern = r'([A-Za-z0-9])[!@#$%&\s]+(?=[A-Za-z0-9])'
text = re.sub(pattern, r'\1 ', decoded)
print(text)
