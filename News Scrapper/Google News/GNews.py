from GoogleNews import GoogleNews
from newspaper import Article
import pandas as pd
import nltk
nltk.download('punkt')




googlenews=GoogleNews()
googlenews.set_lang('fr')
googlenews.enableException(True)
googlenews.search('Duhaime')

#googlenews.set_period('1d')
#googlenews.set_encode('utf-8')

result=googlenews.result()



#print(result)
print(googlenews.get_links())

array_articles = []
df=pd.DataFrame(result)
print(df.head())
for ind in df.index:
    dict={}
    article = Article(df['link'][ind])
    article.download()
    article.parse()
    article.nlp()
    dict['Date']=df['date'][ind]
    dict['Media']=df['media'][ind]
    dict['Title']=article.title
    dict['Article']=article.text
    dict['Summary']=article.summary
    array_articles.append(dict)
news_df=pd.DataFrame(list)
news_df.to_excel("articles.xlsx")