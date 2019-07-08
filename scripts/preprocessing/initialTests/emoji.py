import pandas as pd
import csv
import re
import pprint


my_csv = pd.read_csv('Tweets/sk-slovenčina-no-lang.csv', delimiter=',', names=["created_at", "lang", "screen_name", "location", "full_text", "urls", "tags", "mentions", "retweet_count", "favorite_count"])
dict = {}
# regular expression object
# \U escape sequence

emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)
print(my_csv["full_text"])
for index, row in my_csv.iterrows():
    sentence = row["full_text"]
    x = re.findall(emoji_pattern, sentence)
    # re.findall() module is used when you want to iterate over the lines of the file,
    # it will return a list of all the matches in a single step
    # re.match finds something at the beginning of the string and return a match object
    # re.search searches for the pattern throughout the string.
    # Problem: detected only the first occurrence of any emoji in a row
    #print(x)
    if x:
        if sentence not in dict.keys():
            dict[sentence] = x
        else:
            dict[sentence] = dict[sentence] + x
pp = pprint.PrettyPrinter(indent=1)
pp.pprint(dict)

# re.match returns a re.Match object with indicated the span and the match
# span() returns a tuple, with start and end position of the nth captured group.
# match='' returns the nth captured group.
# by specifying .group() it returns only the match as value of dict.
