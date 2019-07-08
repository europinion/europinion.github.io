import rdflib
from rdflib import Graph, URIRef
import pprint

default_graph = URIRef('http://this_is_the_name_of_our_graph')
graph = Graph(identifier=default_graph)
graph.parse("Scripts/Named_Graph/mt-1.txt", format="nt")
for stmt in graph:
    pprint.pprint(stmt)
#output in mt-1-parsed.txt

# The final lines show how rdflib represents the statements in the file. The statements themselves are just length-3 tuples; and the subjects, predicates, and objects are all rdflib types.
# https://rdflib.readthedocs.io/en/3.4.0/intro_to_graphs.html
# the name of a named graph is a URIRef

#print(graph)
# output: <http://this_is_the_name_of_our_graph> a rdfg:Graph;rdflib:storage [a rdflib:Store;rdfs:label 'IOMemory'].
