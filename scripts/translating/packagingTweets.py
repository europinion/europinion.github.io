# -*- coding: utf-8 -*-
import pandas as pd
import requests
import time

# Note:
# If you receive a very long error message, the contingent of your key is used.
# Follow the lastSuccess instruction to continue at the point of interruption.

# Here you add the key. (A key can be used for 1.000.000 chr/day and 10.0000.000 chr/month)
key = "trnsl.1.1.20190625T093708Z.70b13e001e10312c.9f1c4c27c2359a0dc21d61fc4613c8b0c7887d8d"

# Uncomment one file at a time to avoid issues.
filenames = [   # DONE "Data/Translated_Tweets/bg-български.csv", DONE
                # DONE "Data/Translated_Tweets/cs-čeština.csv", DONE
                # DONE "Data/Translated_Tweets/da-dansk.csv", DONE
                # DONE "Data/Translated_Tweets/de-deutsch.csv", DONE
                # DONE "Data/Translated_Tweets/el-ελληνικά.csv", DONE
                "Data/Preprocessed_Tweets/en-english.csv",
                # DONE "Data/Translated_Tweets/es-español.csv", DONE
                # DONE "Data/Translated_Tweets/et-eesti_keel.csv", DONE
                # DONE "Data/Translated_Tweets/fi-suomi.csv", DONE
                # DONE "Data/Translated_Tweets/fr-français.csv", DONE
                # DONE "Data/Translated_Tweets/ga-gaeilge.csv", DONE
                # DONE "Data/Translated_Tweets/hr-hrvatski.csv", DONE
                # DONE "Data/Translated_Tweets/hu-magyar.csv", DONE
                # DONE "Data/Translated_Tweets/it-italiano.csv", DONE
                # DONE "Data/Translated_Tweets/lt-lietuvių_kalba.csv", DONE
                # DONE "Data/Translated_Tweets/lv-latviešu_valoda.csv", DONE
                # DONE "Data/Translated_Tweets/mt-malti.csv", DONE
                # DONE "Data/Translated_Tweets/nl-nederlands.csv", DONE
                # DONE "Data/Translated_Tweets/pl-polski.csv", DONE
                # DONE "Data/Translated_Tweets/pt-português.csv", DONE
                # DONE "Data/Translated_Tweets/ro-română.csv", DONE
                # DONE "Data/Translated_Tweets/sk-slovenčina.csv", DONE
                # DONE "Data/Translated_Tweets/sl-slovenščina.csv", DONE
                # DONE "Data/Translated_Tweets/sv-svenska.csv" DONE
            ]

### Function for Saving to CSV ###
# Nothing to do here.
# def saving(response, index):
#     responseJSON = response.json()
#     responseLIST = responseJSON["text"][0].split(" [!] ")
#
#     start = index - len(responseLIST) + 1
#     end = index
#     indices = list(range(start, end + 1))
#     position = 0
#
#     for tweet in indices:
#         df.at[tweet,"english"] = responseLIST[position]
#         position += 1
#
#     print("Saving... lastSuccess:", index)
#     df.to_csv(file, sep = ";", index=False)

### Sending Packages to Yandex ###
# Nothing to do here.
# def sending(package, index):
#     text = " [!] ".join(package)
#     lang = "en"
#     data = {"key": key, "text": text, "lang": lang}
#
#     try:
#         response = requests.post("https://translate.yandex.net/api/v1.5/tr.json/translate", data=data)
#         saving(response, index)
#     except requests.exceptions.RequestException as e:
#         print(e)
#         print("Waiting for 60 sec.")
#         time.sleep(60)
#         sending(package, index)

### Packaging Tweets with the Seperator " [!] " ###
# Nothing to do here.
# def packaging(lastSuccess = -1):
#     package = []
#     packageCount = 0
#
#     for index, row in df.iterrows():
#         if sum(len(tweets) for tweets in package) < 8500 and index > lastSuccess:
#             package.append(row["parsed_text"])
#         if sum(len(tweets) for tweets in package) >= 8500 and len(df.index) - 1 != index:
#             packageCount += 1
#             print("Sending... Package nr.", packageCount, "– Progress:", round((index / (len(df.index) - 1)) * 100, 2), "%")
#             sending(package, index)
#             package = []
#             time.sleep(5)
#         elif len(df.index) - 1 == index:
#             packageCount += 1
#             print("Sending LAST package for", file, "– Progress:", round((index / (len(df.index) - 1)) * 100, 2), "%")
#             sending(package, index)
#             time.sleep(5)


### Triggering the Chain of Functions ###
# Here you have to uncomment/comment the code depending on if you use a NEW FILE or OLD File.
# For OLD FILES you have to add the lastSuccess in the brackets of packaging(lastSuccess)
for file in filenames:
    ### Two types of files:

    ### NEW FILE – NOT opened before -> has no "english" column
    df = pd.read_csv(file, delimiter = ";", encoding="utf-8", skiprows=1, names = ["created_at", "lang", "screen_name", "location", "full_text", "urls", "tags", "mentions", "retweet_count", "favorite_count", "parsed_text", "emoji"])
    df["english"] = ""
    df.to_csv(file, sep = ";", index=False)
    ### OLD FILE – partially translated
    # df = pd.read_csv(file, delimiter = ";", encoding="utf-8", skiprows=1, names = ["created_at", "lang", "screen_name", "location", "full_text", "urls", "tags", "mentions", "retweet_count", "favorite_count", "parsed_text", "emoji", "english"])

    ### NEW FILE – leave brackets blank: packaging()
    ### OLD FILE – input is lastSuccess: packaging(lastSuccess)
    #packaging()
