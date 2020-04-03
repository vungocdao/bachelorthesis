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

text = 'my lovely pat has one of the great voices of her generation i have listened to this cd for years and i still love it when im in a good mood it makes me feel better a bad mood just evaporates like sugar in the rain this cd just oozes life vocals are jusat stuunning and lyrics just kill one of lifes hidden gems this is a desert isle cd in my book why she never made it big is just beyond me everytime i play this no matter black white young old male female everybody says one thing who was that singing .'
'despite the fact that i have only played a small portion of the game the music i heard plus the connection to chrono trigger which was great as well led me to purchase the soundtrack and it remains one of my favorite albums there is an incredible mix of fun epic and emotional songs those sad and beautiful tracks i especially like as theres not too many of those kinds of songs in my other video game soundtracks i must admit that one of the songs lifea distant promise has brought tears to my eyes on many occasionsmy one complaint about this soundtrack is that they use guitar fretting effects in many of the songs which i find distracting but even if those werent included i would still consider the collection worth it.'
'i bought this charger in jul  and it worked ok for a while the design is nice and convenient however after about a year the batteries would not hold a charge might as well just get alkaline disposables or look elsewhere for a charger that comes with batteries that have better staying power.'
'check out maha energys website their powerex mhcf charger works in  minutes for rapid charge with option for slower charge better for batteries and they have  mah batteries.'

tone_analysis = tone_analyzer.tone(
    {'text': text},
    content_type='application/json').get_result()

print(json.dumps(tone_analysis, indent=2))
