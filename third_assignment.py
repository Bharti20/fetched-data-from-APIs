import requests

user = 'Bharti20'
token = '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'

response = requests.get('https://api.github.com/user/repos?per_page=100', auth=(user, token))
allData = response.json()

list_of_repos = []

for dic in allData:
    for key in dic:
        if key == 'name':
            list_of_repos.append(dic[key])
print(list_of_repos)