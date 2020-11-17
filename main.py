# ぐるなびAPI

import requests
import pprint
url = '' #APIのURL
params = {}
params['keyid'] = '' #キー
params['freeword'] = '' #検索ワード

response = requests.get(url, params)
# 返ってきた情報を代入     宛先     送る情報

# print(response.json())
# pprint.pprint(response.json())

results = response.json()
len(results['rest']) #10

restaurants = results['rest']
print(restaurants[0]['name'])
























