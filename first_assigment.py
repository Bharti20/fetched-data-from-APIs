import requests
import json

url = 'https://datausa.io/api/data?drilldowns=Nation&measures=Population'
response = requests.get(url)
allData = response.text
data_in_dic=json.loads(allData)
mainList = []

for i in data_in_dic['data']:
    list = []
    for key in i:
        if key == 'Nation' or key == 'Year' or key == 'Population':
            list.append(i[key])
    mainList.append(list)
print(mainList)
