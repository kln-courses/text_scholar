#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" tutorial: import xml from folder """
__author__      = "K.L. Nielbo"
# a look at a hierarchical data format
import io
filename = '/home/kln/Documents/education/text_scholar/data/xml/1807_65.xml'
with io.open(filename,'r',encoding = 'utf8') as f:
    xmlplain = f.read() 
f.closed
print xmlplain
print 'the tm gods prefer plain text'.upper()

# read lines in xml document from folder on filepath 
import os
from lxml import html
filepath = "/home/kln/Documents/education/text_scholar/data/xml/"
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
    docs.append(lignes)    

# test 1
ii = 0
print titles[ii]
for ligne in docs[ii]: print ligne

# more systematic
import os
from lxml import html    
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
        # filter empty entries after <l> tag
        lignes = filter(None, lignes)    
        docs.append(lignes)
    # collapse lines to string
    docs_str =[]
    for doc in docs:
        docs_str.append(" ".join(doc))
    return docs, titles, docs_str

# test 2
docs, titles, docs_str = xml_folder("/home/kln/Documents/education/text_scholar/data/xml/")

ii = 0
print titles[ii]
for ligne in docs[ii]: print ligne
print docs_str[ii]