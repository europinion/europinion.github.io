#### It is maybe necessary to install the libraries first. You can install them as any other Python library.
from TwitterAPI import TwitterAPI, TwitterPager
import csv


#### Note:
#### The script downloads ALL tweets between the 27th May and 2nd June (included). Hence, we have all tweets of one week.
#### We can always decide on a later point whether we use all the tweets or not.
#### The script does wait if you have reached your request limit. The script indicates the time it has to wait in seconds.


#### First, input Twitter app/api credentials
consumer_key='aH6EHC8TvJ6S1AksCciYDVy57'
consumer_secret='tCdV1EmwzipXAsm3bIZ34vaI1FRvz6LKPfCb5ewHjY8vvd8dGo'
access_token_key='271587996-zaxPcnNBKFWLwKApEfEfwMwbxbes1KkHYdaVRldE'
access_token_secret='C4Zto7L8bybTvcZbDSw4kJtbEjB7t3TgMXfVOajqp2oZZ'

# Nothing to do here.
PRODUCT = '30day'
LABEL = 'EURELsandbox'

#### Then, rename the file "en-english.csv" to the language which you are downloading.
#### In this way we have separated files for each language.
csvFile = open('download.csv', 'a')

# Nothing to do here. The next lines just prepare the file, i.e. it names the columns.
csvWriter = csv.writer(csvFile)
csvWriter.writerow(["created_at", "lang", "screen_name", "location", "full_text", "urls", "tags", "mentions", "retweet_count", "favorite_count"])

# Nothing to do here.
count_tweets = 0
count_retweets = 0
api = TwitterAPI(consumer_key,consumer_secret,access_token_key,access_token_secret)

#### Now change 'European Elections' in q to the correct query terms. (Leave -filter:retweets as it is.)
#### Lastly, either change lang="en" to the correct value or delete lang="en" completely if language is not supported.
#### In our gDoc you find a list of the correct Twitter values for lang="". If there is no value in the list, the language is not supported.
data = TwitterPager(api, 'tweets/search/%s/:%s' % (PRODUCT, LABEL),
                {'query':'European Elections lang:en', 'fromDate':'201905270001', 'toDate':'201905281401'})

for tweet in data.get_iterator():
    if 'retweeted_status' not in tweet:
        count_tweets += 1
        user = tweet['user']
        list_tags = [tags['text'] for tags in tweet['entities']['hashtags']]
        list_tags = ', '.join(list_tags)
        list_mentions = [mentions['screen_name'] for mentions in tweet['entities']['user_mentions']]
        list_mentions = ', '.join(list_mentions)
        list_urls = [urls['expanded_url'] for urls in tweet['entities']['urls']]
        list_urls = ', '.join(list_urls)

        if 'extended_tweet' in tweet:
            csvWriter.writerow([tweet['created_at'], tweet['lang'], user['screen_name'], user['location'], tweet['extended_tweet']['full_text'], list_urls, list_tags, list_mentions, tweet['retweet_count'], tweet['favorite_count']])
        elif 'text' in tweet:
            csvWriter.writerow([tweet['created_at'], tweet['lang'], user['screen_name'], user['location'], tweet['text'], list_urls, list_tags, list_mentions, tweet['retweet_count'], tweet['favorite_count']])

        print('Yeah, found already a total of',count_tweets,'tweets!')

    elif 'retweeted_status' in tweet:
        count_retweets += 1
        print('Ups, that adds up to',count_retweets,'useless retweets...')
