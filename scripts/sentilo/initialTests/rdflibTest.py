# import time
# import csv
# import requests
# import pandas as pd
# from rdflib import ConjunctiveGraph, Graph, URIRef
# import pprint
#
# default_graph = URIRef("http://this_is_the_name_of_our_graph")
# graph = ConjunctiveGraph(identifier=default_graph)
#
# graph.parse("Scripts/Sentilo/Test/test.xml", format='xml')
# graph.parse("Scripts/Sentilo/Test/vacation.xml", format='xml')
#
# graph.serialize(destination='output.xml', format='xml')



### Goal:
# RDF/XML file which contains a graph interlinking all tweets.
# The tweets have links to hasNegScore, hasPosScore, hasAvgScore (for hasNegScore and hasPosScore),



import rdflib
from rdflib import *
from rdflib.graph import Graph, ConjunctiveGraph
from rdflib.plugins.memory import IOMemory

RDF = rdflib.namespace.RDF

ns = Namespace("http://europinion.com#")

de = URIRef("http://europinion.com/lang/de#")
en = URIRef("http://europinion.com/lang/en#")

tweet_1=URIRef("http://europinion.com/tweet/1#")
tweet_2=URIRef("http://europinion.com/tweet/2#")

store = IOMemory()

g = ConjunctiveGraph(store=store)
g.bind("europinion",ns)

tweet_1_graph = ConjunctiveGraph(store=store, identifier=tweet_1)
tweet_1_graph.parse("Scripts/Sentilo/Test/test.xml", format='xml')
tweet_1_graph.add((tweet_1, ns['is'], URIRef("http://ontologydesignpatterns.org/ont/sentilo.owl#opinion_sentence_5694c67c5712ff52b91f9d258368273a")))
tweet_1_graph.add((URIRef("http://ontologydesignpatterns.org/ont/sentilo.owl#opinion_sentence_5694c67c5712ff52b91f9d258368273a"), ns['hasLang'], de))

tweet_2_graph = ConjunctiveGraph(store=store, identifier=tweet_2)
tweet_2_graph.parse("Scripts/Sentilo/Test/vacation.xml", format='xml')
tweet_2_graph.add((tweet_2, ns['is'], URIRef("http://ontologydesignpatterns.org/ont/sentilo.owl#opinion_sentence_7fa636acd54bb89c9c7dcf518cc18242")))
tweet_2_graph.add((URIRef("http://ontologydesignpatterns.org/ont/sentilo.owl#opinion_sentence_7fa636acd54bb89c9c7dcf518cc18242"), ns['hasLang'], en))

#enumerate contexts
for c in tweet_1_graph.contexts():
    print("-- %s " % c)

# test = g.value(RDF.Description)
# print("+++", test)
# print([c for c in tweet_1_graph.triples((None, RDF.Description, None))])

for c in tweet_1_graph.objects(predicate=RDF.type):
    tweet_1_graph.add((tweet_1, ns['hasContent'], c))

#separate graphs
print(tweet_1_graph.serialize(format='n3'))
print("===================")
print(tweet_2_graph.serialize(format='n3'))
print("===================")
#enumerate contexts
for c in g.contexts():
    print("-- %s " % c)

#full graph
print(g.serialize(format='n3'))
g.serialize(destination='output.xml', format='xml')
