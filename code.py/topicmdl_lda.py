#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" tutorial: flat topic model using latent Dirichlet allocation """
__author__      = "K.L. Nielbo"

import os
os.chdir("/home/kln/Documents/education/text_scholar/code.py")
import textscholar as ts

somedir = "/home/kln/Documents/education/text_scholar/data/txt/"

texts, titles = ts.vanilla_folder(somedir)
texts = ts.norm_unicode(texts)
texts = ts.tokenize_list(texts)
#texts = ts.stem_list(texts)

from collections import defaultdict
import numpy as np
def prune_token(unigrams,mxper = 95,mnper = 0):
    frequency = defaultdict(int)
    for doc in unigrams:
        for unigram in doc:
            frequency[unigram] += 1
    freqs = [val for val in frequency.values()]
    mx = np.percentile(freqs, mxper)
    mn = np.percentile(freqs, mnper)
    unigrams_prune = [[unigram for unigram in doc if (frequency[unigram] > mn and frequency[unigram] <= mx)] for doc in unigrams]
    return unigrams_prune

texts = prune_token(texts,99)

print titles[0]
print texts[0]

#from gensim.utils import chunkize
#def chunk_token(unigrams,n):
#    chunks = []
#    for doc in unigrams:
#        clen = len(doc)/n
#        for chunk in chunkize(doc,clen):
#            chunks.append(chunk)
#    return chunks
# docschunks = chunk_token(docstoken,5)

## train LDA model
from gensim import corpora, models
# bag-of-words
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(chunk) for chunk in texts]
# for reproducibility
fixed_seed = 1234
# import numpy as np
np.random.seed(fixed_seed)
# train model on k topics
k = 20
mdl = models.LdaModel(corpus, id2word=dictionary, num_topics=k, chunksize=3125, passes=25, update_every=0, alpha=None, eta=None, decay=0.5, distributed=False)
# print topics
for i in range(0,k):
    print 'Topic', i+1
    print(mdl.show_topic(i,15))
    print('-----')
