# update save file
resave <- function(..., list = character(), file) {
  previous  <- load(file)
  var.names <- c(list, as.character(substitute(list(...)))[-1L])
  for (var in var.names) assign(var, get(var, envir = parent.frame()))
  save(list = unique(c(previous, var.names)), file = file)
}
# slice text in n bins
slice_text <- function(text,bin){
  sliced.text.l <- split(text, cut(1:length(text),bin))
}
# sentence tokenizer
token_sent <- function(text, lang = "en") {
  sentannotator <- openNLP::Maxent_Sent_Token_Annotator(language = lang)
  text <- NLP::as.String(text)# convert to string
  sentbound <- NLP::annotate(text, sentannotator)
  sentences <- text[sentbound]# extract sentences
  return(sentences)# return sentences
}
# caps on first letter in char vector
capname <- function(name.v){
  paste(toupper(substr(name.v, 1, 1)), substr(name.v, 2, nchar(name.v)), sep="")
}
# remove sparse terms by setting minimum representation in documents
docsparse <- function(mindocs,dtm){
  n = length(row.names(dtm))
  sparse <- 1 - mindocs/n;
  dtmreduce <- tm::removeSparseTerms(dtm, sparse)
  return(dtmreduce)
}

# compute column variance in matrix
colVars <- function(x, na.rm=FALSE, dims=1, unbiased=TRUE, SumSquares=FALSE,
                    twopass=FALSE) {
  if (SumSquares) return(colSums(x^2, na.rm, dims))
  N <- colSums(!is.na(x), FALSE, dims)
  Nm1 <- if (unbiased) N-1 else N
  if (twopass) {x <- if (dims==length(dim(x))) x - mean(x, na.rm=na.rm) else
    sweep(x, (dims+1):length(dim(x)), colMeans(x,na.rm,dims))}
  (colSums(x^2, na.rm, dims) - colSums(x, na.rm, dims)^2/N) / Nm1
}


# compute row variance in matrix
rowVars <- function(x) {
  rowSums((x - rowMeans(x))^2)/(dim(x)[2] - 1)
}

# prune dtm on percentile
prune <- function(dtm, mxper, mnper = 0){
  freq <- slam::col_sums(as.matrix(dtm))
  per <- quantile(freq, c(mnper,mxper))
  idx <- (freq >= per[1]) & (freq <= per[2])
  dtm = dtm[,idx]
  return(dtm)
}