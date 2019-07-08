import json
import re
import statistics

langDictPos = {'bg':[],'cs':[],'da':[],'de':[],'el':[],'en':[],'es':[],'et':[],'fi':[],'fr':[],'ga':[],'hr':[],'hu':[],'it':[],'lt':[],'lv':[],'mt':[],'nl':[],'pl':[],'pt':[],'ro':[],'sk':[],'sl':[],'sv':[]}
langDictNeg = {'bg':[],'cs':[],'da':[],'de':[],'el':[],'en':[],'es':[],'et':[],'fi':[],'fr':[],'ga':[],'hr':[],'hu':[],'it':[],'lt':[],'lv':[],'mt':[],'nl':[],'pl':[],'pt':[],'ro':[],'sk':[],'sl':[],'sv':[]}

langList = []
posList = []
negList = []

with open('visualisation_3_lang.json') as json_file:
    data = json.load(json_file)
    for tweets in data['results']['bindings']:
        print('Saving')
        eurEnding = re.findall('(\d\d\d\d.*\d)', tweets['tweet']['value'])[0]
        for key in langDictPos:
            if key in eurEnding:
                langDictPos[key].append(float(tweets['p_score']['value']))
                langDictNeg[key].append(float(tweets['n_score']['value']))

for key in langDictPos:
    langList.append(key)

    if len(langDictPos[key]) > 0:
        meanPos = statistics.mean(langDictPos[key])
        posList.append(meanPos)
    else:
        posList.append(0)

    if len(langDictNeg[key]) > 0:
        meanNeg = statistics.mean(langDictNeg[key])
        print(meanNeg)
        negList.append(meanNeg)
    else:
        negList.append(0)

dataOutput = {"langList": langList, "postList": posList, "negList": negList}

with open('data.txt', 'w') as outfile:
    print('Saving')
    json.dump(dataOutput, outfile)
