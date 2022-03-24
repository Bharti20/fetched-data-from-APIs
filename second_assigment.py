import requests

url = 'http://httpbin.org/get'
response = requests.get(url) 
allData = response.json()
print(allData['headers']['User-Agent'])
print(allData["origin"])
