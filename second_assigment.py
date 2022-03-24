import requests
import json

url = 'http://httpbin.org/get'
response = requests.get(url)
print(response.encoding)
# data_in_string = response.text
# allData = json.loads(data_in_string)
# print(allData['headers']['User-Agent'])
# print(allData["origin"])
