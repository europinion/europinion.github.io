from rdflib import Graph

g = Graph()
g.parse("/Users/SeverinBurg/Google/University/Gangemi/Scripts/Sentilo/test.txt", format="xml")
g.parse("/Users/SeverinBurg/Google/University/Gangemi/Scripts/Sentilo/demo.nt", format="nt")

len(g)

import pprint
for stmt in g:
    pprint.pprint(stmt)
