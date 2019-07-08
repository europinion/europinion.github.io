import pandas as pd
import csv
import re
import pprint


my_csv = pd.read_csv('Tweets/sk-slovenčina-no-lang.csv', delimiter=',', names=["created_at", "lang", "screen_name", "location", "full_text", "urls", "tags", "mentions", "retweet_count", "favorite_count"])

dict = {}

emoji_pattern = re.compile("[" u"\U00002702-\U0001F9F0" "]+", flags=re.UNICODE)

for index, row in my_csv.iterrows():
    sentence = row["full_text"]
    x = re.findall(emoji_pattern, sentence)
    if x:
        if sentence not in dict.keys():
            dict[sentence] = x
        else:
            dict[sentence] = dict[sentence] + x
            
pp = pprint.PrettyPrinter(indent=1)
pp.pprint(dict)
