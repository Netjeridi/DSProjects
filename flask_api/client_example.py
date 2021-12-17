import json
import requests

# url = 'http://Localhost:8000/predict'
# #url = 'http://Localhost:8000/files'

# #or url = 'http://127.0.0.1:8000/model'

# request_data = json.dumps({'model': 'knn', 'data': [1], 'filename': '20211019-1625-supportpal-ticket_tag.csv'})
# response = requests.post(url,request_data)
# print(response.text)


url = 'http://Localhost:8000/run'
#url = 'http://Localhost:8000/files'

# or url = 'http://127.0.0.1:8000/model'

request_data = json.dumps({'model': 'linear_regression',
                           'data': [[1]]
                           })
response = requests.post(url, request_data)
print(response.text)

url = 'http://Localhost:8000/list_models'

response = requests.get(url)
print(response.text)
