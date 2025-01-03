import newspaper 
from newspaper import Article


#cnn_paper = newspaper.build('https://ici.radio-canada.ca/')

url = 'https://ici.radio-canada.ca/nouvelle/2010366/westjet-poilievre-discours-syndicat-excuses'
article = Article(url)
print(article.keywords)

article.download()

article.parse()


print(article.keywords)