import pandas as pd
import json
import re

df = pd.read_csv('assets/visualisations/sample-graph.csv', delimiter = ";", encoding="utf-8", skiprows=1, names = ['tweetnr', 'created_at', 'lang', 'screen_name', 'location', 'full_text', 'urls', 'tags', 'mentions', 'retweet_count', 'favorite_count', 'parsed_text', 'emoji', 'english', 'clean'])

langDict = {'bg':10,'cs':11,'da':12,'de':13,'el':14,'en':15,'es':16,'et':17,'fi':18,'fr':19,'ga':20,'hr':21,'hu':22,'it':23,'lt':24,'lv':25,'mt':26,'nl':27,'pl':28,'pt':29,'ro':30,'sk':31,'sl':32,'sv':33}

nodes = []
links = []

data = {"nodes":nodes, "links":links}

newNode = {"id":str(2019),"group":1}
data['nodes'].append(newNode)

for key in langDict:
    groupID = langDict[key]
    newLink = {"source":str(2019),"target":str(key),"predicate":"eur:lang"}
    data['links'].append(newLink)

    newNode = {"id":str(key),"group":groupID}
    data['nodes'].append(newNode)

for index, row in df.iterrows():
    groupID = langDict[row['lang']]

    tweetID = str('/2019'+'/'+row['lang']+'/'+str(row['tweetnr'])+'/')
    newLink = {"source":str(row['lang']),"target":tweetID,"predicate":"eur:hasTweet"}
    data['links'].append(newLink)

    newNode = {"id":tweetID,"group":groupID}
    data['nodes'].append(newNode)

    datestamp = re.findall('(\d\d\d\d-\d\d-\d\d)', row['created_at'])[0]
    newLink = {"source":tweetID,"target":str(datestamp),"predicate":"eur:hasDate"}
    data['links'].append(newLink)
    if not any(node['id'] == str(datestamp) for node in data['nodes']):
        newNode = {"id":str(datestamp),"group":groupID}
        data['nodes'].append(newNode)

    timestamp = re.findall('(\d\d:\d\d:\d\d)', row['created_at'])[0]
    newLink = {"source":tweetID,"target":str(timestamp),"predicate":"eur:hasTime"}
    data['links'].append(newLink)
    if not any(node['id'] == str(timestamp) for node in data['nodes']):
        newNode = {"id":str(timestamp),"group":groupID}
        data['nodes'].append(newNode)

    newLink = {"source":tweetID,"target":str(row['screen_name']),"predicate":"eur:createdBy"}
    data['links'].append(newLink)
    if not any(node['id'] == str(row['screen_name']) for node in data['nodes']):
        newNode = {"id":str(row['screen_name']),"group":groupID}
        data['nodes'].append(newNode)

    if pd.isnull(row['location']) == False:
        newLink = {"source":tweetID,"target":str(row['location']),"predicate":"eur:hasLocation"}
        data['links'].append(newLink)
        if not any(node['id'] == str(row['location']) for node in data['nodes']):
            newNode = {"id":str(row['location']),"group":groupID}
            data['nodes'].append(newNode)

    newLink = {"source":tweetID,"target":str(row['full_text']),"predicate":"eur:hasText"}
    data['links'].append(newLink)
    if not any(node['id'] == str(row['full_text']) for node in data['nodes']):
        newNode = {"id":str(row['full_text']),"group":groupID}
        data['nodes'].append(newNode)

    if pd.isnull(row['urls']) == False:
        urlsList = row['urls'].split(',')
        for item in urlsList:
            tmp = item.strip()
            newLink = {"source":tweetID,"target":str(tmp),"predicate":"eur:hasURL"}
            data['links'].append(newLink)
            if not any(node['id'] == str(tmp) for node in data['nodes']):
                newNode = {"id":str(tmp),"group":groupID}
                data['nodes'].append(newNode)

    if pd.isnull(row['tags']) == False:
        tagsList = row['tags'].split(',')
        for item in tagsList:
            tmp = item.strip()
            newLink = {"source":tweetID,"target":str(tmp),"predicate":"eur:hasHashtag"}
            data['links'].append(newLink)
            if not any(node['id'] == str(tmp) for node in data['nodes']):
                newNode = {"id":str(tmp),"group":groupID}
                data['nodes'].append(newNode)

    if pd.isnull(row['mentions']) == False:
        mentionsList = row['mentions'].split(',')
        for item in mentionsList:
            tmp = item.replace(" ", "")
            newLink = {"source":tweetID,"target":str(tmp),"predicate":"eur:hasMention"}
            data['links'].append(newLink)
            if not any(node['id'] == str(tmp) for node in data['nodes']):
                newNode = {"id":str(tmp),"group":groupID}
                data['nodes'].append(newNode)

    if row['retweet_count'] != 0:
        newLink = {"source":tweetID,"target":str(row['retweet_count']),"predicate":"eur:hasRetweet"}
        data['links'].append(newLink)
        if not any(node['id'] == str(row['retweet_count']) for node in data['nodes']):
            newNode = {"id":str(row['retweet_count']),"group":groupID}
            data['nodes'].append(newNode)

    if row['favorite_count'] != 0:
        newLink = {"source":tweetID,"target":str(row['favorite_count']),"predicate":"eur:isFavorite"}
        data['links'].append(newLink)
        if not any(node['id'] == str(row['favorite_count']) for node in data['nodes']):
            newNode = {"id":str(row['favorite_count']),"group":groupID}
            data['nodes'].append(newNode)

    newLink = {"source":tweetID,"target":str(row['parsed_text']),"predicate":"eur:hasParsed"}
    data['links'].append(newLink)
    if not any(node['id'] == str(row['parsed_text']) for node in data['nodes']):
        newNode = {"id":str(row['parsed_text']),"group":groupID}
        data['nodes'].append(newNode)

    if pd.isnull(row['emoji']) == False:
        emojiList = row['emoji'].split(',')
        for item in emojiList:
            tmp = item.strip()
            newLink = {"source":tweetID,"target":str(tmp),"predicate":"eur:hasEmoji"}
            data['links'].append(newLink)
            if not any(node['id'] == str(tmp) for node in data['nodes']):
                newNode = {"id":str(tmp),"group":groupID}
                data['nodes'].append(newNode)

    newLink = {"source":tweetID,"target":str(row['english']),"predicate":"eur:hasTranslation"}
    data['links'].append(newLink)
    if not any(node['id'] == str(row['english']) for node in data['nodes']):
        newNode = {"id":str(row['english']),"group":groupID}
        data['nodes'].append(newNode)

    print('building...')

print(data)

with open('sampleGraph2.json', 'w') as output:
    json.dump(data, output)
