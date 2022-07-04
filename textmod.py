from keys import *
import requests
import json


def textmod(text):
    data = {
      'text': f'{text}',
      'mode': 'standard',
      'lang': 'en',
      'api_user': f'{api_user}',
      'api_secret': f'{api_secret}'
    }
    r = requests.post('https://api.sightengine.com/1.0/text/check.json', data=data)
    output = json.loads(r.text)
    profan_list = []
    for word in output['profanity']['matches']:
        profan_list.append(word['type'])
    return profan_list