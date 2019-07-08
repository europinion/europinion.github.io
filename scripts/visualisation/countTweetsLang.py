import pandas as pd

df = pd.read_csv("Data/all-translated.csv", delimiter = ";", encoding="utf-8", skiprows=1, names = ["created_at", "lang", "screen_name", "location", "full_text", "urls", "tags", "mentions", "retweet_count", "favorite_count", "parsed_text", "emoji", "english"])
langDict = {'bg':0,'cs':0,'da':0,'de':0,'el':0,'en':0,'es':0,'et':0,'fi':0,'fr':0,'ga':0,'hr':0,'hu':0,'it':0,'lt':0,'lv':0,'mt':0,'nl':0,'pl':0,'pt':0,'ro':0,'sk':0,'sl':0,'sv':0}

for index, row in df.iterrows():
    for key in langDict:
        if key == row['lang']:
            langDict[key] += 1
            print(langDict[key])

print(langDict)
