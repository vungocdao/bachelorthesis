import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions

authenticator = IAMAuthenticator('PtJi8o9UyO8koiyqOJ-JOQPDFURQI9H8lKI8WzQxHc6Y')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    authenticator=authenticator
)

natural_language_understanding.set_service_url('https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com/instances/17e005b5-ebde-489d-8483-60fbd1ea1cfd')

for i in range(15):
    f = open("Restaurant_Reviews" + str(i) + ".txt", "r")

    text = f.readline()

    sentiment_analysis = natural_language_understanding.analyze(text = text, features=Features(sentiment=SentimentOptions()), language = "en").get_result()
    print(json.dumps(sentiment_analysis, indent=2))
