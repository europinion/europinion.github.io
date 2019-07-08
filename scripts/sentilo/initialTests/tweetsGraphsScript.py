# curl is a command line tool to transfer data to or from a server, using any of the supported protocols
# we use curl for creating a collection of files from each of the tweets
# create programmatically a list of curls and launch them with a sleep in the middle to avoid server bottlenecks

import time
import csv
import requests
import pandas as pd
from rdflib import Graph, URIRef
import pprint
# the tweets we launch to sentilo are already translated at this point and free of #,@,emoticons or we can pass direclty here
# only the textual part of the tweet. Where do I specify this?

### RESPONSE: We will specify this by selecting the respective column here: sentence = row["full_text"]

#with open('it-italiano.csv', 'r') as csvfile: #final_csvFile # get tweets from the single csv file with all the tweets
#    reader = csv.reader(csvfile)
#    for row in reader:
#        sentence = "Germania, Nahles lascia la guida dell'Spd dopo la debacle alle elezioni europee"
#        url = 'http://wit.istc.cnr.it/stlab-tools/sentilo/service?text=sentence&format=format'
#        response = requests.get(url, sentence)
        #nt_response = response.nt()
#        response.encoding = 'utf-8'
#        time.sleep(1)
        #### the sytem will wait upon the response for 1 sec before moving on
#        print(response)
#### launch each of them to sentilo to get its graph

my_csv = open('it-italiano.csv', 'a', encoding="utf-8")
### pd.read_csv will read our final csv containing all the tweets in all the languages
my_csv = pd.read_csv('Data/all-translated.csv', delimiter = ';', encoding="utf-8", skiprows=1, names = ["created_at", "lang", "screen_name", "location", "full_text", "urls", "tags", "mentions", "retweet_count", "favorite_count", "parsed_text", "emoji", "english"])

file = open("Scripts/Sentilo/test.txt","w")

default_graph = URIRef('http://this_is_the_name_of_our_graph')
graph = Graph(identifier=default_graph)

for index, row in my_csv.iterrows():
    sentence = row["english"]
    print(sentence)
    format = 'application/rdf+xml'
    data = {'text': sentence, 'format': format}
    headers = {
        'Accept': 'application/rdf+xml'
    }
    r = requests.get('http://wit.istc.cnr.it/stlab-tools/sentilo/service', params=data, headers=headers)

    file.write(r.text)
    file.close()
    time.sleep(1)
    break

file = open("Scripts/Sentilo/test.txt","r")
graph.parse(file.read())
print(file.read())
print(graph)
