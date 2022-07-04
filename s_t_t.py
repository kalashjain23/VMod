import requests
from keys import *


def text(link):
    base_url = "https://api.assemblyai.com/v2/transcript"
    json = {
        "audio_url": link
    }
    headers = {
        "authorization": f"{s_t_key}",
        "content-type": "application/json"
    }
    trans_id = (requests.post(base_url, json=json, headers=headers)).json()["id"]

    endpoint = f"https://api.assemblyai.com/v2/transcript/{trans_id}"
    data = (requests.get(endpoint, headers=headers)).json()

    while data['status'] != 'completed':
        data = (requests.get(endpoint, headers=headers)).json()
        if data['status'] == 'error':
            return 'error'

    return data['text']
