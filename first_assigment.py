import requests

url = 'https://datausa.io/api/data?drilldowns=Nation&measures=Population'
response = requests.get(url)
allData = response.json()
mainList = []

for i in allData['data']:
    list = []
    for key in i:
        if key == 'Nation' or key == 'Year' or key == 'Population':
            list.append(i[key])
    mainList.append(list)
print(mainList)
