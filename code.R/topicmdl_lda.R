# LDA
rm(list = ls())
wd <- '/home/kln/Documents/education/text_scholar'
setwd(wd)
source('code.R/util_fun.R')
# necessary
library(tm)
library(topicmodels)
# make life easier
library(plyr)
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
books.dtm <- docsparse(2,books.dtm)
dim(books.dtm)
summary(col_sums(books.dtm))
books.dtm <- prune(books.dtm,.75,1)
summary(col_sums(books.dtm))

### estimate number of topics (optimal k estimation)
k = 100
#progress.bar <- create_progress_bar("text")
#progress.bar$init(k)
best.mdl <- list()
# perplex.mat <- matrix(0,k-1,2)
for(i in 2:k){
  best.mdl[[i-1]] <- LDA(books.dtm, i)
  print(paste('k =',i, sep = ' '))
#  progress.bar$step()
#  save(best.mdl, file = 'someLdaMdl.RData')
}
#save(best.mdl,file = 'estimate_k.RData')
load('estimate_k.RData')
perplex.mat <- as.matrix(unlist(lapply(best.mdl, perplexity)))
plot(perplex.mat, main= 'Parameter estimation', xlab = 'k', ylab = 'Perplexity')

# unpack model
# ten most likely terms in each topic
terms(best.mdl[[18]],10)

# two dominant topics for all documents
top2 <- topics(best.mdl[[18]],2)
colnames(top2) <- filenames
print(top2)


### train model wit k = 18
mdl <- LDA(books.dtm, 18)



