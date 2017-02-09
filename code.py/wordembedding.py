#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" tutorial: word embedding """
__author__      = "K.L. Nielbo"

import io, os, re, unicodedata

# sort on integer
num = re.compile(r'(\d+)')
def numericalsort(value):
    parts = num.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

somedir = "/home/kln/Documents/education/text_scholar/data/txt/"

# read files line by line
files = sorted(os.listdir(somedir), key = numericalsort)
doc_lines = []
os.chdir(somedir)
for file in files:
    with io.open(file,'r',encoding = 'utf8') as f:    
        lines = [l.strip('\n') for l in f.readlines()]
        for i in range(len(lines)):
            line = lines[i]
            line = unicodedata.normalize('NFKD', line)#.encode('ascii','ignore')
            line = re.sub(r"\d", ' ',line)
            line = re.sub(r'\W+', ' ',line)
            lines[i] = line
        doc_lines.append(lines)

# flatten list
doc_lines = [ligne for lignes in doc_lines for ligne in lignes]
os.chdir("/home/kln/Documents/education/text_scholar/code.py")
import textscholar as ts
linesnorm = ts.norm_unicode(doc_lines)
linestoken = ts.tokenize_list(linesnorm)
# remove empty lines
linestoken = [l for l in linestoken if l != []]
# train model
import gensim
mdl = gensim.models.Word2Vec(linestoken, min_count=5,size=100)
# look at results
print mdl.most_similar('gud')
print mdl.most_similar('guds')

mdl.most_similar(positive=['kvinde', 'konge'], negative=['mand'])
mdl.doesnt_match("gud jesus odin christ".split())
mdl.similarity('gud','odin')

import matplotlib.pyplot as plt
plt.matshow(mdl['jesus'].reshape((10,10)), fignum = 100, cmap=plt.cm.gray)
