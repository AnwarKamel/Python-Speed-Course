# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 09:33:53 2020

@author: LinuxPC
"""
import json
# read json file
with open('data/person.json') as f:
    data = json.load(f)

print(data)