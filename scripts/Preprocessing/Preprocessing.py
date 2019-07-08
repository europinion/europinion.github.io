# -*- coding: utf-8 -*-
import pandas as pd
import preprocessor as p
import string
import nltk
from nltk.corpus import stopwords
import re

# df = pd.read_csv('Preprocessed_Tweets/_Parts/fr-français-9.csv', delimiter = ',', encoding="utf-8", names = ["created_at", "lang", "screen_name", "location", "full_text", "urls", "tags", "mentions", "retweet_count", "favorite_count"])
#
# df["created_at"] = df["created_at"].map(lambda x: x.replace('+0000',''))
# df["created_at"] = df["created_at"].map(lambda x: x.replace('Mon',''))
# df["created_at"] = df["created_at"].map(lambda x: x.replace('Tue',''))
# df["created_at"] = df["created_at"].map(lambda x: x.replace('Wed',''))
# df["created_at"] = df["created_at"].map(lambda x: x.replace('Thu',''))
# df["created_at"] = df["created_at"].map(lambda x: x.replace('Fri',''))
# df["created_at"] = df["created_at"].map(lambda x: x.replace('Sab',''))
# df["created_at"] = df["created_at"].map(lambda x: x.replace('Sun',''))
# df["created_at"] = df["created_at"].map(lambda x: x.replace('2019',''))
# df["created_at"] = df["created_at"].map(lambda x: x.strip())
#
# for index, row in df.iterrows():
#     line = row["created_at"]
#     row["created_at"] = line[:7] + '2019 ' + line[7:]
#
#     print(row["created_at"])
#
# df.to_csv(r'Preprocessed_Tweets/_Parts/fr-français-9.csv', index=False)

# Combine CSV files
filenames = [   "Data/3_Superclean_Tweets/bg-български.csv",
                "Data/3_Superclean_Tweets/cs-čeština.csv",
                "Data/3_Superclean_Tweets/da-dansk.csv",
                "Data/3_Superclean_Tweets/de-deutsch.csv",
                "Data/3_Superclean_Tweets/el-ελληνικά.csv",
                "Data/3_Superclean_Tweets/en-english.csv",
                "Data/3_Superclean_Tweets/es-español.csv",
                "Data/3_Superclean_Tweets/et-eesti_keel.csv",
                "Data/3_Superclean_Tweets/fi-suomi.csv",
                "Data/3_Superclean_Tweets/fr-français.csv",
                "Data/3_Superclean_Tweets/ga-gaeilge.csv",
                "Data/3_Superclean_Tweets/hr-hrvatski.csv",
                "Data/3_Superclean_Tweets/hu-magyar.csv",
                "Data/3_Superclean_Tweets/it-italiano.csv",
                "Data/3_Superclean_Tweets/lt-lietuvių_kalba.csv",
                "Data/3_Superclean_Tweets/lv-latviešu_valoda.csv",
                "Data/3_Superclean_Tweets/mt-malti.csv",
                "Data/3_Superclean_Tweets/nl-nederlands.csv",
                "Data/3_Superclean_Tweets/pl-polski.csv",
                "Data/3_Superclean_Tweets/pt-português.csv",
                "Data/3_Superclean_Tweets/ro-română.csv",
                "Data/3_Superclean_Tweets/sk-slovenčina.csv",
                "Data/3_Superclean_Tweets/sl-slovenščina.csv",
                "Data/3_Superclean_Tweets/sv-svenska.csv"
            ]
lis = []

# for file in filenames:
#     df = pd.read_csv(file, delimiter = ";", encoding="utf-8", skiprows=1, names = ["created_at", "lang", "screen_name", "location", "full_text", "urls", "tags", "mentions", "retweet_count", "favorite_count", "parsed_text", "emoji", "english"])
#     lis.append(df)
#     print(lis)
#
# combined_csv = pd.concat(lis, axis=0, ignore_index=True)
# combined_csv.to_csv(r'Data/Translated_Tweets/all-translated2.csv', sep = ";", index=False)


# filenames = [   # "Data/Preprocessed_Tweets/bg-български.csv",
                # "Data/Preprocessed_Tweets/cs-čeština.csv",
                # "Data/Preprocessed_Tweets/da-dansk.csv",
                # "Data/Preprocessed_Tweets/de-deutsch.csv",
                # "Data/Preprocessed_Tweets/el-ελληνικά.csv",
                # "Data/Preprocessed_Tweets/en-english.csv",
                # "Data/Preprocessed_Tweets/es-español.csv",
                # "Data/Preprocessed_Tweets/et-eesti_keel.csv",
                # "Data/Preprocessed_Tweets/fi-suomi.csv",
                # "Data/Preprocessed_Tweets/fr-français.csv",
                # "Data/Preprocessed_Tweets/ga-gaeilge.csv",
                # "Data/Preprocessed_Tweets/hr-hrvatski.csv",
                # "Data/Preprocessed_Tweets/hu-magyar.csv",
                # "Data/Preprocessed_Tweets/it-italiano.csv",
                # "Data/Preprocessed_Tweets/lt-lietuvių_kalba.csv",
                # "Data/Preprocessed_Tweets/lv-latviešu_valoda.csv",
                # "Data/Preprocessed_Tweets/mt-malti.csv",
                # "Data/Preprocessed_Tweets/nl-nederlands.csv",
                # "Data/Preprocessed_Tweets/pl-polski.csv",
                # "Data/Preprocessed_Tweets/pt-português.csv",
                # "Data/Preprocessed_Tweets/ro-română.csv",
                # "Data/Preprocessed_Tweets/sk-slovenčina.csv",
                # "Data/Preprocessed_Tweets/sl-slovenščina.csv",
                # "Data/Preprocessed_Tweets/sv-svenska.csv"
#            ]

# emoji_pattern = re.compile("[" u"\U00002702-\U0001F9F0" "]+", flags=re.UNICODE)
# p.set_options(p.OPT.URL, p.OPT.MENTION, p.OPT.HASHTAG)
#
# for file in filenames:
#     df = pd.read_csv(file, delimiter = ";", encoding="utf-8", skiprows=1, names = ["created_at", "lang", "screen_name", "location", "full_text", "urls", "tags", "mentions", "retweet_count", "favorite_count"])
#
#     df["parsed_text"] = ""
#     df["emoji"] = ""
#
#     for index, row in df.iterrows():
#         tmp_parsed_text = p.clean(row["full_text"])
#         tmp_emoji = re.findall(emoji_pattern, tmp_parsed_text)
#
#         for emoji in tmp_emoji:
#             tmp_parsed_text = tmp_parsed_text.replace(emoji,"")
#
#         tmp_emoji = ", ".join(tmp_emoji)
#         df.at[index,"emoji"] = tmp_emoji
#
#         tmp_parsed_text= re.sub(" +", " ", tmp_parsed_text)
#         df.at[index,"parsed_text"] = tmp_parsed_text
#
#     print(file)
#     df.to_csv(file, sep = ";", index=False)


for file in filenames:
    df = pd.read_csv(file, delimiter = ";", encoding="utf-8", skiprows=1, names = ['created_at', 'lang', 'screen_name', 'location', 'full_text', 'urls', 'tags', 'mentions', 'retweet_count', 'favorite_count', 'parsed_text', 'emoji', 'english'])

    df["clean"] = ""

    for index, row in df.iterrows():
        stop_words = stopwords.words('english')
        sentence = str(row["english"])
        sentence = sentence.lower()
        sentence = re.sub(r'\d+', '', sentence)
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        sentence = sentence.strip()
        sentence = [word for word in sentence.split() if word not in stop_words]
        sentence = ' '.join(sentence)

        df.at[index,"clean"] = sentence

    print(file)
    df.to_csv(file, sep = ";", index=False)
