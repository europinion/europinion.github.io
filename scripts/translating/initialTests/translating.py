# -*- coding: utf-8 -*-
import os, requests, uuid, json
import pandas as pd

subscriptionKey = "4f4db45ca5dc44288e5939fec767a186"
base_url = 'https://api.cognitive.microsofttranslator.com'
path = '/translate?api-version=3.0'
params = '&to=en'
constructed_url = base_url + path + params

headers = {
    'Ocp-Apim-Subscription-Key': subscriptionKey,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

filenames = [   # 'Preprocessed_Tweets/bg-български.csv', done
                # 'Preprocessed_Tweets/cs-čeština.csv', done
                # 'Preprocessed_Tweets/da-dansk.csv', done
                # 'Preprocessed_Tweets/de-deutsch.csv', error 3260
                # 'Preprocessed_Tweets/el-ελληνικά.csv', error 1259
                # 'Preprocessed_Tweets/en-english.csv',
                'Preprocessed_Tweets/es-español.csv',
                'Preprocessed_Tweets/et-eesti_keel.csv',
                'Preprocessed_Tweets/fi-suomi.csv',
                'Preprocessed_Tweets/fr-français.csv',
                'Preprocessed_Tweets/ga-gaeilge.csv',
                'Preprocessed_Tweets/hr-hrvatski.csv',
                'Preprocessed_Tweets/hu-magyar.csv',
                'Preprocessed_Tweets/it-italiano.csv',
                'Preprocessed_Tweets/lt-lietuvių_kalba.csv',
                'Preprocessed_Tweets/lv-latviešu_valoda.csv',
                'Preprocessed_Tweets/mt-malti.csv',
                'Preprocessed_Tweets/nl-nederlands.csv',
                'Preprocessed_Tweets/pl-polski.csv',
                'Preprocessed_Tweets/pt-português.csv',
                'Preprocessed_Tweets/ro-română.csv',
                'Preprocessed_Tweets/sk-slovenčina.csv',
                'Preprocessed_Tweets/sl-slovenščina.csv',
                'Preprocessed_Tweets/sv-svenska.csv'
            ]

for file in filenames:
    df = pd.read_csv(file, delimiter = ";", encoding="utf-8", skiprows=1, names = ["created_at", "lang", "screen_name", "location", "full_text", "urls", "tags", "mentions", "retweet_count", "favorite_count", "parsed_text", "emoji"])

    print("OPEN", file)
    counter = 0

    df["english"] = ""

    for index, row in df.iterrows():
        counter += 1
        print(file, "Translating no", counter)
        body = [{
            'text' : row["parsed_text"]
        }]
        request = requests.post(constructed_url, headers=headers, json=body)
        response = request.json()
        df.at[index,"english"] = response[0]["translations"][0]["text"]

    print(file)
    df.to_csv(file, sep = ";", index=False)
