import json
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator("wWb3QxJovOh6mfXU_a-vjLo4QpYQnvJpfDBbVEhiCWqv")
tone_analyzer = ToneAnalyzerV3 (
    version = '2017-09-21',
    authenticator=authenticator
)

tone_analyzer.set_service_url('https://api.eu-de.tone-analyzer.watson.cloud.ibm.com/instances/d967bd97-be2d-4b92-a8b4-79c1c54ae9a2')

for i in range(1000):
    f = open("Amazon_Reviews" + str(i) + ".txt", "r")

    text = f.readline()

    tone_analysis = tone_analyzer.tone(
	   {'text': text},
	      content_type='application/json').get_result()
    print(json.dumps(tone_analysis, indent=2))
