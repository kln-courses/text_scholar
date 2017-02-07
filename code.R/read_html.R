library(XML)
# read and parse html file
# no noise
url = 'http://apiolaza.net/babel'
# noise
url = 'http://www.biblestudytools.com/job/'
doc.html = htmlTreeParse(url,
           useInternal = TRUE)
# extract paragraphs and ublist
doc.text = unlist(xpathApply(doc.html, '//p', xmlValue))
# Replace all \n by spaces
doc.text = gsub('\\n', ' ', doc.text)
# doc.text = gsub('\\r', ' ', doc.text)
#  character vector
doc.text = paste(doc.text, collapse = ' ')
