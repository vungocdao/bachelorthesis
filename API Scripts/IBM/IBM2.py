import json
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import pandas as pd

authenticator = IAMAuthenticator("wWb3QxJovOh6mfXU_a-vjLo4QpYQnvJpfDBbVEhiCWqv")
tone_analyzer = ToneAnalyzerV3 (
    version = '2017-09-21',
    authenticator=authenticator
)

tone_analyzer.set_service_url('https://api.eu-de.tone-analyzer.watson.cloud.ibm.com/instances/d967bd97-be2d-4b92-a8b4-79c1c54ae9a2')


df = pd.read_csv("Amazon_Reviews.csv")
df2 = df['Review'].head(5)
list = df2.tolist()

text = list

for i in range (len(list)):
    text = list[i]
    tone_analysis = tone_analyzer.tone(
        {'text': text},
        content_type='application/json').get_result()
    print(json.dumps(tone_analysis, indent=2))
