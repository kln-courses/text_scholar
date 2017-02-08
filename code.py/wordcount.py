#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
""" tutorial: word counts """
__author__      = "K.L. Nielbo"

# basic word count for string
from collections import Counter
doc = 'Peter er Peter. Er Peter er også lidt Madsen?'
wf = Counter(doc.lower().split())
print wf

# import file
import re
filepath = '/home/kln/Documents/education/text_scholar/data/txt/31_12469.txt'
words = re.findall(r'\w+', open(filepath).read().lower())
wf = Counter(words)

# show common words
print 'ten most common words:'
print wf.most_common(10)

# print all wf
for key in wf:
   print "Term: %s , Frequency: %s" % (key, wf[key])

# make specific query
query = ['loke', 'odin', 'aser', 'jesus']
for e in query:
    if wf.has_key(e):
        print e + ': ' + str(wf.get(e))
    else:
        print e + ': ' + str(0)

# a bit of plotting
from numpy import linspace
from math import log
# frequency
d = sorted(wf.values(), reverse = True)
dr = [f/sum(d) for f in d]
dlog = [log(f,10) for f in d]
# rank
x = linspace(1,len(d),len(d)); 
xlog = [log(i,10) for i in x]

import matplotlib.pyplot as plt
f, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=False,figsize=(12, 4))
ax1.plot(x,d)
ax2.plot(x,dr)
ax3.scatter(xlog,dlog)
ax1.set_title('Linear')
ax2.set_title('Weighted Linear')
ax3.set_title('LogLog')
ax1.set_ylabel('Frequency')
ax1.set_xlabel('Rank')
ax2.set_xlabel('Rank')
ax3.set_xlabel('Rank')
plt.show()
f.savefig('/home/kln/Documents/education/text_scholar/resources/zipf.png')