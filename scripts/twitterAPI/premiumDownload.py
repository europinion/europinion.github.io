from TwitterAPI import TwitterAPI, TwitterPager
import csv

### Twitter API Credentials ###
consumer_key='###'
consumer_secret='###'
access_token_key='###'
access_token_secret='###'

### Product Selection ###
PRODUCT = '30day'
LABEL = 'EURELsandbox'

### Filepath for Storing ###
csvFile = open('download.csv', 'a')

csvWriter = csv.writer(csvFile)
csvWriter.writerow(["created_at", "lang", "screen_name", "location", "full_text", "urls", "tags", "mentions", "retweet_count", "favorite_count"])

count_tweets = 0
count_retweets = 0
api = TwitterAPI(consumer_key,consumer_secret,access_token_key,access_token_secret)

data = TwitterPager(api, 'tweets/search/%s/:%s' % (PRODUCT, LABEL),
                {'query':'European Elections lang:en', 'fromDate':'201905270001', 'toDate':'201906022359'})

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
