#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" tutorial: import plain text from folder """
__author__      = "K.L. Nielbo"

import io
filename = '/home/kln/Documents/education/text_scholar/data/txt/31_12469.txt'
with io.open(filename,'r',encoding = 'utf8') as f:
    vanilla = f.read() 
    f.closed
print vanilla

import os, re
filepath = "/home/kln/Documents/education/text_scholar/data/txt/"
files = os.listdir(filepath)
os.chdir(filepath)
docs = []
titles = []
for file in files:
    with io.open(file,'r',encoding = 'utf8') as f:
        vanilla = f.read()
        docs.append(vanilla)
        titles.append(re.sub(r'\.txt$', '', file))
        f.closed

import io, os, re
def vanilla_folder(filepath):
    files = os.listdir(filepath)
    os.chdir(filepath)
    docs = []
    titles = []
    for file in files:
        with io.open(file,'r',encoding = 'utf8') as f:
            vanilla = f.read()
            docs.append(vanilla)
            titles.append(re.sub(r'\.txt$', '', file))
            f.closed
    return docs, titles
        

docs, titles = vanilla_folder("/home/kln/Documents/education/text_scholar/data/txt/")