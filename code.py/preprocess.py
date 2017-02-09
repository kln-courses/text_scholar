#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" tutorial: clean list of strings """
__author__      = "K.L. Nielbo"

import io, os, re

filename = '/home/kln/Documents/education/text_scholar/data/txt/31_12469.txt'
with io.open(filename,'r',encoding = 'utf8') as f:
    vanilla = f.read() 
    f.closed
print vanilla[0:1000]

# normalize and clean text
from unidecode import unidecode
vanillanorm = unidecode(vanilla)
print vanillanorm[0:1000]
vanillanorm = vanillanorm.lower()
print vanillanorm[0:1000]
regex = re.compile("['\-,\.!?<>0-9]")
vanillanorm = regex.sub('',vanillanorm)
print vanillanorm[0:1000]

# for list of unicode
import re
from unidecode import unidecode
def norm_unicode(docs):
    normdocs = []
    regex = re.compile("['()\*\-,\.!?<>0-9]")
    for doc in docs:
        doc = doc.lower()
        #doc = unidecode(doc)
        doc = regex.sub('',doc)
        normdocs.append(doc)
    return normdocs
    
os.chdir("/home/kln/Documents/education/text_scholar/code.py/")
from readvanilla import vanilla_folder

docs, titles = vanilla_folder("/home/kln/Documents/education/text_scholar/data/txt/")
test = docs[0:9]
docsnorm = norm_unicode(docs)
docsnorm[0]
# tokenization
token = docsnorm[0].split()
print token

def tokenize_list(docs):
    unigrams = [[w for w in doc.split()] for doc in docs]
    return unigrams

docstoken = tokenize_list(docsnorm)
print docstoken[0]

## remove stopwords
from nltk.corpus import stopwords
sw = stopwords.words("danish")
print sw
len(token)
token = [word for word in token if word not in sw] 
len(token)

from nltk.corpus import stopwords
def stopfilter_list(docstoken, lang = "english"):
    sw = stopwords.words(lang)   
    # sw = io.open("/home/kln/Documents/education/text_scholar/resources/stopwords_da.txt",'r',encoding = 'utf8').read().lower().split() 
    output = []
    for tokens in docstoken:
        output.append([token for token in tokens if token not in sw])
    return output

docstoken = stopfilter_list(docstoken, 'danish')

### prune m top and n bottom words
from collections import defaultdict
import numpy as np
def prune_n(docs, mxn, mnn = 1):
    frequency = defaultdict(int)
    for doc in docs:
        for token in doc:
            frequency[token] += 1
    freqs = sorted([val for val in frequency.values()], reverse = True)
    mx = freqs[mxn - 1]
    mn = freqs[- mnn]
    output = [[token for token in doc if frequency[token] >= mn and frequency[token] <= mx] for doc in docs]
    return output

len(docstoken[0])
docstoken = prune_n(docstoken, 10)
len(test[0])

# stemming
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("danish", ignore_stopwords = True)
token = [stemmer.stem(w) for w in token] 
print token

def stem_list(docstoken):
    docsstem = [[stemmer.stem(w) for w in token] for token in docstoken]
    return docsstem
    
docsstem = stem_list(docstoken) 
print docsstem[0]

# working with dataframes for metadata
import pandas as pd
import numpy as np
filepath = "/home/kln/Documents/education/text_scholar/data/adl_index.txt"
metadata = pd.read_table(filepath, header = None, encoding = 'utf-8')
metadata.head()
titles[0:5]

titles_df = pd.DataFrame(np.zeros(shape = (len(titles), 2)))
for i in range(len(titles)):
    titles_df.iloc[i,:] = map(int,titles[i].split('_'))
idx = metadata.iloc[:,0] == titles_df.iloc[0,0]
target_df = metadata.loc[idx,:]
idx = target_df.iloc[:,1] == titles_df.iloc[0,1]
print target_df.loc[idx,:]
print docsstem[0]

metadata = pd.read_table(filepath, header = None, encoding = 'utf-8')
def get_metadata(metadata, titles, docnum):
    titles_df = pd.DataFrame(np.zeros(shape = (len(titles), 2)))    
    for i in range(len(titles)):
        titles_df.iloc[i,:] = map(int,titles[i].split('_'))
    target_df = metadata.loc[metadata.iloc[:,0] == titles_df.iloc[docnum,0],:]    
    return (target_df.loc[target_df.iloc[:,1] == titles_df.iloc[docnum,1],:]).reset_index()
    
print get_metadata(metadata, titles, 0)
print docsstem[0]




