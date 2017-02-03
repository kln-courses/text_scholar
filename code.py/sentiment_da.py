#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" tutorial: sentiment analysis in Danish """
__author__      = "K.L. Nielbo"

import os
os.chdir("/home/kln/Documents/education/text_scholar/code.py")
from textscholar import vanilla_folder

somedir = "/home/kln/Documents/education/text_scholar/data/txt/"
docs, titles = vanilla_folder(somedir)
# remove non alphabetic characters and casefold
import re
def norm_unicode(docs):
    normdocs = []
    regex = re.compile("['()\*\-,\.!?<>0-9]")
    for doc in docs:
        #doc = unidecode(doc).lower()
        doc = regex.sub('',doc)
        normdocs.append(doc.lower())
    return normdocs

docsnorm = norm_unicode(docs)
from afinn import Afinn

text = docsnorm[100]
print text
# modernize document
regex = re.compile("aa")
text = regex.sub(u'å',text)
print text
# apply Afinn da 32
afinn = Afinn(language='da')
sentvec = []
for token in text.split():
    wordsent = afinn.score(token)
    sentvec.append(wordsent)
    print token, wordsent
import numpy as np    
sentvec = np.asarray(sentvec)
print np.sum(sentvec)
# length normalize
print np.sum(sentvec)/len(sentvec)
# lazy is good
print afinn.score(text)
# length normalized score
print afinn.score(text)/len(text.split())

# DIY
import pandas as pd
sentpath = '/home/kln/Documents/education/text_scholar/resources/AFINN-da-32.txt'
da32 = pd.read_csv(sentpath, skiprows = 0, sep='\t', index_col = 0)
print da32.head()
print da32.score.min()
print da32.score.max()
da32dict = da32.iloc[:,0].to_dict()
print da32dict.keys()[0:9]
print da32dict.values()[0:9]
def afinnscr(text):
    words = text.split()
    sent_vec = [da32dict.get(word.lower(), 0.0) for word in words]
    avg_scr = sum(sent_vec) / len(words)
    return sent_vec, avg_scr
sentvec, avg_scr = afinnscr(text)

# visualize
import matplotlib.pyplot as plt
plt.figure(1)
h = plt.plot(sentvec)
plt.setp(h, 'color', 'r', 'linewidth', 2.0)
plt.xlabel('Narrative Time')
plt.ylabel('Sentiment')
plt.grid(True) 

# now make your own dictionary









