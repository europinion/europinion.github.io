from TwitterAPI import TwitterAPI, TwitterPager
import csv

consumer_key='aH6EHC8TvJ6S1AksCciYDVy57'
consumer_secret='tCdV1EmwzipXAsm3bIZ34vaI1FRvz6LKPfCb5ewHjY8vvd8dGo'
access_token_key='271587996-zaxPcnNBKFWLwKApEfEfwMwbxbes1KkHYdaVRldE'
access_token_secret='C4Zto7L8bybTvcZbDSw4kJtbEjB7t3TgMXfVOajqp2oZZ'

PRODUCT = '30day'
LABEL = 'EURELsandbox'

csvFile = open('download.csv', 'a')

csvWriter = csv.writer(csvFile)
csvWriter.writerow(["created_at", "lang", "screen_name", "location", "full_text", "urls", "tags", "mentions", "retweet_count", "favorite_count"])

count_tweets = 0
count_retweets = 0
api = TwitterAPI(consumer_key,consumer_secret,access_token_key,access_token_secret)

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
