# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 08:57:52 2020

@author: AnwarKamel
"""

# Flatten a list of lists
data = [
        [1, 2 ], [3, 5], [8, 10]]
result = []
for x in data:
    for y in x:
        result.append(y)

print(result)