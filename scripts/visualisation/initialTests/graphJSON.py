import json
import rdflib
from rdflib import *

print('loading...')
graph = rdflib.Graph()
graph.open('store', create=True)
graph.parse('big_sample.rdf')

nodes = []
links = []

data = {"nodes":nodes, "links":links}

eur = Namespace('http://www.europinion.com/')


# for subject, predicate, object in graph:
#     if (predicate == eur.lang) or (predicate == eur.hasTweet):
#         if not any(node['id'] == str(subject) for node in data['nodes']):
#             newNode = { "id":str(subject)}
#             data['nodes'].append(newNode)
#         if not any(node['id'] == str(object) for node in data['nodes']):
#             newNode = {"id":str(object)}
#             data['nodes'].append(newNode)

#         newLink = {"id1":str(subject),"id2":str(object)}
#         data['links'].append(newLink)
#     print('building...')

# print(data)


for subject, predicate, object in graph:
    if (predicate == eur.lang) or (predicate == eur.hasTweet):
        if not any(node['id'] == str(subject) for node in data['nodes']):
            newNode = { "id":str(subject),"name":str(subject),"val":1}
            data['nodes'].append(newNode)
        if not any(node['id'] == str(object) for node in data['nodes']):
            newNode = {"id":str(object),"name":str(object),"val":1}
            data['nodes'].append(newNode)

        newLink = {"source":str(subject),"target":str(object)}
        data['links'].append(newLink)
    print('building...')

print(data)

with open('graph.json', 'w') as output:
    json.dump(data, output)
