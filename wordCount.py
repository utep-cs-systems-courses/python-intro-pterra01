#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 13:04:38 2020

@author: pterrazas
"""

import sys
import re
import string

def get_list(text):
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    text = re.sub('[{}]'.format(string.punctuation), ' ', text)
    words = text.lower().split()
    
    # reading input file
    with open(input_file) as input_txt:
        text = input_txt.read()
        
    # counting of words
    count = {}
    for i in words:
        count.setdefault(i, 0)
        count[i] += 1
        
    # outputting counts
    with open(output_file, 'w') as output_txt:
        for x, y in sorted(count.items()):
            output_txt.write('{} {}\n'.format(x, y))
            
    