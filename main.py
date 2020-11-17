# ぐるなびAPI

import requests
import pprint
url = 'https://api.gnavi.co.jp/RestSearchAPI/v3/'
params = {}
params['keyid'] = 'd69600d69923d84722e8f750f5218525'
params['freeword'] = '小田原駅, 肉'

response = requests.get(url, params)
# 返ってきた情報を代入     宛先     送る情報

# print(response.json())
# pprint.pprint(response.json())

results = response.json()
len(results['rest']) #10

restaurants = results['rest']
print(restaurants[0]['name'])
























