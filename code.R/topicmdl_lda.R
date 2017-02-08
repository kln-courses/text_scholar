# LDA
rm(list = ls())
wd <- '/home/kln/Documents/education/text_scholar'
setwd(wd)
source('code.R/util_fun.R')
# necessary
library(tm)
library(topicmodels)
library(slam)
# build corpus
books.cor  <- Corpus(DirSource('data/txt/', encoding = "UTF-8"), readerControl = list(language = "lat"))
names(books.cor) <- gsub("\\..*","",names(books.cor))# remove ending
filenames <- names(books.cor)
books.cor <- tm_map(books.cor, PlainTextDocument)
books.cor <- tm_map(books.cor, content_transformer(tolower))
books.cor <- tm_map(books.cor, removePunctuation)
books.cor <- tm_map(books.cor, removeNumbers)
books.cor <- tm_map(books.cor, removeWords, stopwords("danish"))
#books.cor <- tm_map(books.cor, stemDocument)
books.cor <- tm_map(books.cor, stripWhitespace)
# document term matrix
books.dtm <- DocumentTermMatrix(books.cor, control = list(minWordLength = 2))
dim(books.dtm)
#books.dtm <- docsparse(2,books.dtm)
# prune dtm
prune <- function(dtm, mxper, mnper = 0){
  freq <- slam::col_sums(as.matrix(dtm))
  per <- quantile(freq, c(mnper,mxper))
  idx <- (freq >= per[1]) & (freq <= per[2])
  dtm = dtm[,idx]
  return(dtm)
  }
books.dtm <- prune(books.dtm,.98)
dim(books.dtm)
### train model wit k = 20
library(tictoc)
set.seed(23)
mdl <- LDA(books.dtm, 20)
# explor model
load('data/lda.RData')
ls("package:topicmodels")
worddist <- get_terms(mdl,10)
topicdist <- get_topics(mdl,10)
colnames(topicdist) <- names(books.cor)
