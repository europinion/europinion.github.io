# -*- coding: utf-8 -*-
import os, requests, uuid, json
import requests
import pandas as pd

filenames = [   "Data/Translated_Tweets/bg-български.csv",
                "Data/Translated_Tweets/cs-čeština.csv",
                "Data/Translated_Tweets/da-dansk.csv",
                "Data/Translated_Tweets/de-deutsch.csv",
                "Data/Translated_Tweets/el-ελληνικά.csv",
                "Data/Translated_Tweets/en-english.csv",
                "Data/Translated_Tweets/es-español.csv",
                "Data/Translated_Tweets/et-eesti_keel.csv",
                "Data/Translated_Tweets/fi-suomi.csv",
                "Data/Translated_Tweets/fr-français.csv",
                "Data/Translated_Tweets/ga-gaeilge.csv",
                "Data/Translated_Tweets/hr-hrvatski.csv",
                "Data/Translated_Tweets/hu-magyar.csv",
                "Data/Translated_Tweets/it-italiano.csv",
                "Data/Translated_Tweets/lt-lietuvių_kalba.csv",
                "Data/Translated_Tweets/lv-latviešu_valoda.csv",
                "Data/Translated_Tweets/mt-malti.csv",
                "Data/Translated_Tweets/nl-nederlands.csv",
                "Data/Translated_Tweets/pl-polski.csv",
                "Data/Translated_Tweets/pt-português.csv",
                "Data/Translated_Tweets/ro-română.csv",
                "Data/Translated_Tweets/sk-slovenčina.csv",
                "Data/Translated_Tweets/sl-slovenščina.csv",
                "Data/Translated_Tweets/sv-svenska.csv"
            ]

key = "trnsl.1.1.20190621T193952Z.6da8da0aedb46113.0c987dadbda84493d69f3a14884c6dee6002556a"

for file in filenames:
    df = pd.read_csv(file, delimiter = ";", encoding="utf-8", skiprows=1, names = ["created_at", "lang", "screen_name", "location", "full_text", "urls", "tags", "mentions", "retweet_count", "favorite_count", "parsed_text", "emoji"])

    print("OPEN", file)
    counter = 0

    df["english"] = ""

    for index, row in df.iterrows():
        counter += 1
        print(file, "Translating no", counter)

        text = row["parsed_text"]
        lang = "en"
        data = {"key": key, "text": text, "lang": lang}

        r = requests.get("https://translate.yandex.net/api/v1.5/tr.json/translate", params=data)
        response = r.json()
        df.at[index,"english"] = response["text"][0]

    print(file)
    df.to_csv(file, sep = ";", index=False)
