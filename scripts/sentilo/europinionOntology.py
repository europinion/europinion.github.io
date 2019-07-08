# -*- coding: utf-8 -*-
import statistics
import json
import time
import requests
import rdflib
import re
import pandas as pd
from rdflib import *
from threading import Thread
from nested_lookup import nested_lookup


filenames = [   # + 'Data/3_Superclean_Tweets/bg-български.csv',
                # + 'Data/3_Superclean_Tweets/cs-čeština.csv',
                # + 'Data/3_Superclean_Tweets/da-dansk.csv',
                # + 'Data/3_Superclean_Tweets/de-deutsch.csv',
                # + 'Data/3_Superclean_Tweets/el-ελληνικά.csv',
                # + 'Data/3_Superclean_Tweets/en-english.csv',
                # + 'Data/3_Superclean_Tweets/es-español.csv',
                #--'Data/3_Superclean_Tweets/et-eesti_keel.csv',
                # + 'Data/3_Superclean_Tweets/fi-suomi.csv',
                # + 'Data/3_Superclean_Tweets/fr-français.csv',
                #--'Data/3_Superclean_Tweets/ga-gaeilge.csv',
                # + 'Data/3_Superclean_Tweets/hr-hrvatski.csv',
                # 2 'Data/3_Superclean_Tweets/hu-magyar.csv',
                # 121,70 'Data/3_Superclean_Tweets/it-italiano.csv',
                # 2 'Data/3_Superclean_Tweets/lt-lietuvių_kalba.csv',
                # 3 'Data/3_Superclean_Tweets/lv-latviešu_valoda.csv',
                #--'Data/3_Superclean_Tweets/mt-malti.csv',
                # + 'Data/3_Superclean_Tweets/nl-nederlands.csv',
                # + 'Data/3_Superclean_Tweets/pl-polski.csv',
                # + 'Data/3_Superclean_Tweets/pt-português.csv',
                # 10 'Data/3_Superclean_Tweets/ro-română.csv',
                # 2 'Data/3_Superclean_Tweets/sk-slovenčina.csv',
                # + 'Data/3_Superclean_Tweets/sl-slovenščina.csv',
                'Data/3_Superclean_Tweets/sv-svenska.csv'
            ]

langDict =  {   'Data/3_Superclean_Tweets/bg-български.csv':'bg',
                'Data/3_Superclean_Tweets/cs-čeština.csv':'cs',
                'Data/3_Superclean_Tweets/da-dansk.csv':'da',
                'Data/3_Superclean_Tweets/de-deutsch.csv':'de',
                'Data/3_Superclean_Tweets/el-ελληνικά.csv':'el',
                'Data/3_Superclean_Tweets/en-english.csv':'en',
                'Data/3_Superclean_Tweets/es-español.csv':'es',
                'Data/3_Superclean_Tweets/et-eesti_keel.csv':'et',
                'Data/3_Superclean_Tweets/fi-suomi.csv':'fi',
                'Data/3_Superclean_Tweets/fr-français.csv':'fr',
                'Data/3_Superclean_Tweets/ga-gaeilge.csv':'ga',
                'Data/3_Superclean_Tweets/hr-hrvatski.csv':'hr',
                'Data/3_Superclean_Tweets/hu-magyar.csv':'hu',
                'Data/3_Superclean_Tweets/it-italiano.csv':'it',
                'Data/3_Superclean_Tweets/lt-lietuvių_kalba.csv':'lt',
                'Data/3_Superclean_Tweets/lv-latviešu_valoda.csv':'lv',
                'Data/3_Superclean_Tweets/mt-malti.csv':'mt',
                'Data/3_Superclean_Tweets/nl-nederlands.csv':'nl',
                'Data/3_Superclean_Tweets/pl-polski.csv':'pl',
                'Data/3_Superclean_Tweets/pt-português.csv':'pt',
                'Data/3_Superclean_Tweets/ro-română.csv':'ro',
                'Data/3_Superclean_Tweets/sk-slovenčina.csv':'sk',
                'Data/3_Superclean_Tweets/sl-slovenščina.csv':'sl',
                'Data/3_Superclean_Tweets/sv-svenska.csv':'sv'
            }

sleep = 0
tries = list()

def initiate(langID):
    global eur, eurGraph, election

    eur = Namespace('http://www.europinion.com/')
    eurGraph = Graph()
    eurGraph.bind('eur', eur, override=False)
    election = URIRef('http://www.europinion.com/2019/')
    lang = URIRef('http://www.europinion.com/2019/' + langID + '/')
    eurGraph.add((election, eur.lang, lang))


def adding(index, row, responseDict, langID):
    global count
    tweetID = URIRef('http://www.europinion.com/2019/' + langID + '/' + str(count))
    langForTweet = URIRef('http://www.europinion.com/2019/' + langID + '/')

    eurGraph.add((langForTweet, eur.hasTweet, tweetID))
    eurGraph.add((tweetID, eur.createdBy, Literal(row['screen_name'])))
    eurGraph.add((tweetID, eur.hasText, Literal(row['full_text'])))
    eurGraph.add((tweetID, eur.hasParsed, Literal(row['parsed_text'])))
    eurGraph.add((tweetID, eur.hasTranslation, Literal(row['english'])))
    eurGraph.add((tweetID, eur.hasLang, Literal(row['lang'])))

    ### Retweets
    if row['retweet_count'] != 0:
        eurGraph.add((tweetID, eur.hasRetweet, Literal(int(row['retweet_count']))))

    ### Favourite
    if row['favorite_count'] != 0:
        eurGraph.add((tweetID, eur.isFavorite, Literal(int(row['favorite_count']))))

    ### Location
    if pd.isnull(row['location']) == False:
        eurGraph.add((tweetID, eur.hasLocation, Literal(row['location'])))

    eurGraph.add((tweetID, eur.hasDate, Literal(row['created_at'],datatype=XSD.date)))
    timestamp = re.findall('(\d\d:\d\d:\d\d)', row['created_at'])[0]
    eurGraph.add((tweetID, eur.hasTime, Literal(timestamp, datatype=XSD.time)))

    ### Emoji
    if pd.isnull(row['emoji']) == False:
        emojiList = row['emoji'].split(',')
        for item in emojiList:
            tmp = item.strip()
            eurGraph.add((tweetID, eur.hasEmoji, Literal(item)))

    ### Mentions
    if pd.isnull(row['mentions']) == False:
        mentionsList = row['mentions'].split(',')
        for item in mentionsList:
            tmp = item.replace(" ", "")
            eurGraph.add((tweetID, eur.hasMention, Literal(tmp)))

    ### URLs
    if pd.isnull(row['urls']) == False:
        urlsList = row['urls'].split(',')
        for item in urlsList:
            tmp = item.strip()
            eurGraph.add((tweetID, eur.hasURL, Literal(tmp)))

    ### Hashtags
    if pd.isnull(row['tags']) == False:
        tagsList = row['tags'].split(',')
        for item in tagsList:
            tmp = item.strip()
            eurGraph.add((tweetID, eur.hasHashtag, Literal(tmp)))

    ### Processing Positive Scores
    posScoreList = nested_lookup('http://ontologydesignpatterns.org/ont/sentilo.owl#hasPosScore', responseDict)
    for item in posScoreList:
        eurGraph.add((tweetID, eur.hasPositiveScore, Literal(float(item[0]['value']))))

    posList = [float(item[0]['value']) for item in posScoreList]
    if len(posList) > 0:
        eurGraph.add((tweetID, eur.hasAvgPositive, Literal(statistics.mean(posList))))

    ### Processing Positive Scores
    negScoreList = nested_lookup('http://ontologydesignpatterns.org/ont/sentilo.owl#hasNegScore', responseDict)
    for item in negScoreList:
        eurGraph.add((tweetID, eur.hasNegativeScore, Literal(float(item[0]['value']))))

    negList = [float(item[0]['value']) for item in negScoreList]
    if len(negList) > 0:
        eurGraph.add((tweetID, eur.hasAvgNegative, Literal(statistics.mean(negList))))

    if ((count%10) == 0) or (index == (len(df.index) - 1)):
        eurGraph.serialize(destination='output_it.xml', format='xml')
        print(langID, 'lastSuccess:', index)
        print(langID, 'lastSaved:', count)
        print(langID, 'Error rate:', ((index-count)/index)*100)


def sending(index, row, langID):
    global count, failure, sleep, lastIndex, tries
    sentence = row['clean']
    format = 'application/rdf+json'
    data = {'text': sentence, 'format': format}
    headers = {
        'Accept': 'application/rdf+json'
    }

    print(langID, 'Sending... Index:', index, '– Progress:', round((index / (len(df.index) - 1)) * 100, 2), '%')

    try:
        r = requests.get('http://wit.istc.cnr.it/stlab-tools/sentilo/service', params=data, headers=headers)
        lastIndex = index
        sleep -= 1
    except requests.exceptions.RequestException as e:
        r = 'retry'
        time.sleep(30)
        sending(index, row, langID)

    if str(r) == '<Response [200]>':
        count += 1
        responseDict = json.loads(r.text)
        adding(index, row, responseDict, langID)
    elif str(r) == 'retry':
        pass
    # elif str(r) == '<Response [502]>':
    #     if sentence not in tries:
    #         print(langID, r)
    #         tries.append(sentence)
    #         print(langID, 'Schedule retry:', sentence)
    #         time.sleep(30)
    #         sleep += 1
    #         sending(index, row, langID)
    #     else:
    #         print(langID, r)
    #         failure = failure.append(row, ignore_index=False)
    #         failure.to_csv('Data/sentilo-failure.csv', sep = ";", index=False)
    #         print(langID, 'Already retried:', sentence)
    else:
        print(langID, r)
        failure = failure.append(row, ignore_index=False)
        failure.to_csv('Data/sentilo-failure.csv', sep = ";", index=False)
        print(langID, 'Failed:', sentence)


def iterating(lastSuccess=-1, lastSaved=-1, langID=None):
    global count, sleep
    threads = []
    count = lastSaved + 1

    for index, row in df.iterrows():
        if index > lastSuccess:
            sleep += 1
            t = Thread(target=sending, args=(index, row, langID,))
            threads.append(t)
            t.start()
            time.sleep(1)

            while sleep == 5:
                time.sleep(0.1)


for file in filenames:
    global count
    global failure

    langID = langDict[file]

    failure = pd.read_csv('Data/sentilo-failure.csv', delimiter = ';', encoding='utf-8', skiprows=1, names = ['created_at', 'lang', 'screen_name', 'location', 'full_text', 'urls', 'tags', 'mentions', 'retweet_count', 'favorite_count', 'parsed_text', 'emoji', 'english', 'clean'])

    df = pd.read_csv(file, delimiter = ';', encoding='utf-8', skiprows=1, names = ['created_at', 'lang', 'screen_name', 'location', 'full_text', 'urls', 'tags', 'mentions', 'retweet_count', 'favorite_count', 'parsed_text', 'emoji', 'english', 'clean'])

    initiate(langID)

    eurGraph.parse('output_it.xml', format='xml')

    ### First try: iterating()
    ### Consecutive try: iterating(lastSuccess, lastSaved)
    iterating(langID=langID)
