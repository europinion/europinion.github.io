import json

dataList = []


with open('Sparql_Queries/visualisation/visualisation_3.json') as json_file:
    data = json.load(json_file)
    for tweets in data['results']['bindings']:
        print('Saving')
        dataList.append({'y':tweets['p_score']['value'], 'x':tweets['n_score']['value']})

with open('data.txt', 'w') as outfile:
    print('Saving')
    json.dump(dataList, outfile)
