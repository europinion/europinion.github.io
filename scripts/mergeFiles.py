from rdflib import Graph

graph = Graph()

graph.parse('output_fr.xml', format='xml')
graph.parse('output_hr.xml', format='xml')
graph.parse('output_hu.xml', format='xml')
graph.parse('output_it.xml', format='xml')
graph.parse('output_lt.xml', format='xml')
graph.parse('output_lv.xml', format='xml')
graph.parse('output_nl.xml', format='xml')
graph.parse('output_pl.xml', format='xml')
graph.parse('output_pt.xml', format='xml')
graph.parse('output_ro.xml', format='xml')
graph.parse('output_sk.xml', format='xml')
graph.parse('output.xml', format='xml')


graph.serialize(destination='merge/output.xml', format='xml')
