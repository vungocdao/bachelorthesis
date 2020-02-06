import deepaffects
from deepaffects.rest import ApiException
from pprint import pprint
import pandas as pd
import json

# API key to access DeepAffects API
deepaffects.configuration.api_key['apikey'] = '5O5rfOOcxmKFfBcqNZJQdRAMWOz6K8Lz'

# Create API Class with sentence that needs to be featurized
data = {
        "content": "Zaphod Beeblebrox is a nice guy"}
api_instance = deepaffects.EmotionApi()


try:
    api_response = api_instance.text_recognise_emotion(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmotionApi->sync_recognise_emotion: %s\n" % e)

# curl -X POST
# "https://proxy.api.deepaffects.com/text/generic/api/latest/sync/text_recognise_emotion?apikey=5O5rfOOcxmKFfBcqNZJQdRAMWOz6K8Lz" -H 'content-type: application/json' -d @JSON_Amazon_Reviews_sample.json
