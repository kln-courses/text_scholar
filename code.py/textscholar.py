#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" describe here """
__author__      = "mr. thump"

import io, os, re
from lxml import html    
from unidecode import unidecode
from nltk.stem.snowball import SnowballStemmer
import pandas as pd
import numpy as np

# TODO
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
# TODO
def xml_folder(filepath):
    files = os.listdir(filepath)
    os.chdir(filepath)
    docs = []
    titles = []
    for file in files:
        print "file import: " + file
        h = html.parse(open(file))
        tei = h.xpath('//l') # lines
        titles.append(h.xpath('//title')[0].text)
        n = len(tei)
        lignes = [None]*n
        for i in range(n):
            lignes[i] =  tei[i].text
        lignes = filter(None, lignes)    
        docs.append(lignes)
    docs_str =[]
    for doc in docs:
        docs_str.append(" ".join(doc))
    return docs, titles, docs_str
# TODO
def norm_unicode(docs):
    normdocs = []
    regex = re.compile("['()\*\-,\.\:!?<>0-9]")
    for doc in docs:
        doc = unidecode(doc).lower()
        doc = regex.sub('',doc)
        normdocs.append(doc)
    return normdocs
# TODO
def tokenize_list(docs):
    unigrams = [[w for w in doc.split()] for doc in docs]
    return unigrams
# TODO
def stem_list(docstoken,lang = "danish"):
    stemmer = SnowballStemmer(lang, ignore_stopwords = True)
    docsstem = [[stemmer.stem(w) for w in token] for token in docstoken]
    return docsstem
# TODO
def get_metadata(metadata, titles, docnum):
    titles_df = pd.DataFrame(np.zeros(shape = (len(titles), 2)))    
    for i in range(len(titles)):
        titles_df.iloc[i,:] = map(int,titles[i].split('_'))
    target_df = metadata.loc[metadata.iloc[:,0] == titles_df.iloc[docnum,0],:]    
    return (target_df.loc[target_df.iloc[:,1] == titles_df.iloc[docnum,1],:]).reset_index()
