import csv
import pprint
import pandas as pd

lang_csv = pd.read_csv("Preprocessed_Tweets/en-english.csv", sep = ";", encoding="utf-8", names = ["created_at", "lang", "screen_name", "location", "full_text", "urls", "tags", "mentions", "retweet_count", "favorite_count"])
hashtag_csv = pd.read_csv("emotion lexicon/hashtag_emotion.csv", sep = ";", encoding = "utf-8", names = ["emotion", "hashtag", "value"])

dict = {}
for index, row in hashtag_csv.iterrows():
    dict[row["hashtag"]] = row["emotion"]

dict_tweet = {}
for index, row in lang_csv.iterrows():
    sentence = str(row["tags"])
    dict_sent = {}
    for word in sentence.split():
        if word in dict.keys():
            dict_sent[word] = dict[word]
        else:
            dict_sent[word] = "no emotion"
        dict_tweet[row["full_text"]] = dict_sent
pp = pprint.PrettyPrinter(indent=1)
pp.pprint(dict_tweet)
