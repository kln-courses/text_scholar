rm(list = ls())
wd <- '/home/kln/Documents/education/text_scholar'
setwd(wd)
library(XML)
# read and parse html file
url = 'http://adl.dk/adl_pub/pg/cv/ShowPgText.xsql?p_udg_id=137&p_sidenr=203&hist=fmO&nnoc=adl_pub'
doc.html = htmlTreeParse(url,
           useInternal = TRUE)
# extract paragraphs and ublist
doc.text = unlist(xpathApply(doc.html, '//p', xmlValue))
print(doc.text)
# Replace all \n by spaces
doc.text = gsub('\\n', ' ', doc.text)
print(doc.text)
# doc.text = gsub('\\r', ' ', doc.text)
#  character vector
doc.text = paste(doc.text, collapse = ' ')
print(doc.text)
# but if txt file in archive 
url = 'http://adl.dk/adl_pub/pg/cv/AsciiPgVaerk2.xsql?nnoc=adl_pub&p_udg_id=137&p_vaerk_id=12469'
filename.v = paste(wd,'/data/sometxt.txt',sep="")
download.file(url, destfile = filename.v)