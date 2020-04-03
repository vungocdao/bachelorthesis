import json
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator("UZSBy08xmA3B_YA809gAvJ80eNfOLMx13lzUPZwjblxS")
tone_analyzer = ToneAnalyzerV3 (
    version = '2017-09-21',
    authenticator=authenticator
)

tone_analyzer.set_service_url('https://api.eu-de.tone-analyzer.watson.cloud.ibm.com/instances/ce90b5f9-4dc4-4857-9727-0d062a5791e3')

for i in range(936):
    f = open("Uber_Ride_Reviews" + str(i) + ".txt", "r")

    text = f.readline()

    tone_analysis = tone_analyzer.tone(
	   {'text': text},
	      content_type='application/json').get_result()
    print(json.dumps(tone_analysis, indent=2))
