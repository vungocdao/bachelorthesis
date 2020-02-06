import requests

url = "https://proxy.api.deepaffects.com/text/generic/api/latest/sync/text_recognise_emotion"

querystring = {"apikey":"gnqC5DPSh7grUYedQb07Gmn5EzfQpbo4"}

headers = {'Content-Type': "application/json",}

response = requests.post(url, json="test.json", headers=headers, params=querystring)

print(response.text)
