import numpy as np
import pandas as pd
from pandas.io.json import json_normalize

pip.main(["install","twitter"])

import twitter
from twitter import Twitter
from twitter import OAuth

ck = "gwEdUQjvo9JDSLMpii205Q06O"
cs = "OlA4PIlLfpZ5HcEAGPOIJx4DwduhmACShoGQ66mJYt4ocxShwX"
at = "823996990329589760-1wW34frljiy7HrWp777qGFzOhEZksMW"
ats = "nzbKJCBUqlCsP6MNe5CFrOzZHo4wcvbubt1nJTqRkvFiB"

oauth = OAuth(at,ats,ck,cs)

api = Twitter(auth=oauth)

search_result = api.search.tweets(q="Olympics",count = 100)
df = json_normalize(search_result,'statuses')
df2 = json_normalize(df['user'])

mid = df['id'].min()
mid = mid -1
search_result2 = api.search.tweets(q="Olympics",count = 100, max_id = mid)
df3 = json_normalize(search_result2,'statuses')
df3['id'].max()
df['id'].min()


df = pd.DataFrame()
mid = 0
for i in range(10):
    if i==0:
        search_result = api.search.tweets(q="Olympics",count = 100)
    else:
        search_result = api.search.tweets(q="Olympics",count = 100, max_id = mid)
    
    dftemp = json_normalize(search_result,'statuses')
    mid = dftemp['id'].min()
    mid = mid - 1
    df = df.append(dftemp,ignore_index=True)

df.shape

    
tweettext = df['text']    

wordlist = pd.DataFrame()

for u in tweettext:
    wsplit = u.split()
    wordlist = wordlist.append(wsplit, ignore_index = True)

wordlist.shape

wordlist.head()    

allword = wordlist.groupby(0).size()
allword.head()

top20word = allword.sort_values(0,ascending=False).head(30)
top20word.plot(kind='bar',title='Top 20 words')

api.followers.ids(screen_name='mcuban')    
ur = api.users.lookup(user_id=964024376839540736)
df4 = json_normalize(ur)
df4['screen_name']

sr3 = api.statuses.user_timeline(screen_name="mcuban")
df5 = json_normalize(sr3)

list(df5.columns)
df5['text']

pip.main(["install","textblob"])
!python -m textblob.download_corpora
from textblob import TextBlob


tx = tweettext[2]
blob = TextBlob(tx)

blob.tags
blob.sentences[0]

blob.sentences[0].words
blob.noun_phrases

verbs = []
for word, tag in blob.tags:
    if tag == 'VB':
        verbs.append(word)

verbs = []
for word, tag in blob.tags:
    if tag == 'VB':
        verbs.append(word)


nouns = []
for word, tag in blob.tags:
    if tag == 'NN':
        nouns.append(word)

blob.sentiment

polarity=[]
subj = []
for t in tweettext:
    tx = TextBlob(t)
    polarity.append(tx.sentiment.polarity)
    subj.append(tx.sentiment.subjectivity)

poltweet = pd.DataFrame({'polarity':polarity,'subjectivity':subj})
poltweet.plot(title = 'Polarity and Subjectivity')

pip.main(["install","newspaper3k"])

url = 'https://www.bloomberg.com/news/articles/2018-02-15/dalio-causes-stir-with-18-billion-surge-in-european-short-bets'
from newspaper import Article
article = Article(url)
article.download()
article.parse()
article.authors
article.publish_date
article.top_image
article.movies
article.keywords
article.summary
article.text
blob2 = TextBlob(article.text)
blob2.noun_phrases
blob2.sentiment

for s in blob2.sentences:
    for w in s.words:
        

