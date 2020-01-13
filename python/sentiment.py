import csv
from textblob import TextBlob
import re
import pandas as pd


#How to just get words out of tweets to use for sentiment analysis. However
#this isn't necessary when using TextBlob


# stopword_set = set(stopwords.words("english"))
#
# # convert to lower case and split
# df_ = df_.str.lower()
# print(df_)
#
# f = lambda x:" ".join(x for x in x.split() if x not in stopword_set)
# df_ = df_.apply(f)
#
# # # remove stopwords
# # df_ = df_.apply(lambda x: [item for item in x if item not in stopword_set])
#
# # keep only words
# regex_pat = re.compile(r'[^a-zA-Z\s]', flags=re.IGNORECASE)
# df_ = df_.str.replace(regex_pat, '')
#
# # join the cleaned words in a list
# df_.str.join("")
# print(df_)
#
# for i in range(5):
#     print(get_tweet_sentiment(df_[i]))



def get_tweet_sentiment(tweet):
    '''
    Utility function to classify sentiment of passed tweet
    using textblob's sentiment method
    '''
    # create TextBlob object of passed tweet text
    analysis = TextBlob(tweet)
    # set sentiment
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

tweets_df = pd.read_csv("sample_english.csv", skipinitialspace=True)
# print (tweets_df.columns.tolist())

# column you are working on
df_ = tweets_df["tweet_text"]
#print(df_)

#To get clean tweets
clean_tweet = []
for text in df_:
    clean_tweet.append(re.sub(r'@\S+|https?://\S+', '', text))
#print(clean_tweet)

#To get the sentiment score and positive/negative ranking
sent_score = []
sentiment = []
for  twt in clean_tweet:
    sent_score.append(TextBlob(twt).sentiment.polarity)
    sentiment.append(get_tweet_sentiment(twt))


#Puts the tweets in a dataframe and exports as csv.
tw_sentiment = pd.DataFrame({
    "tweet": clean_tweet,
    "sentiment": sentiment,
    "polarity_score": sent_score
})
#print(tw_sentiment)
#tw_sentiment.to_csv('tw_sentiment.csv', encoding='utf-8', index=False)
