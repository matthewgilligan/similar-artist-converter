import os
import requests

API_KEY = os.environ.get('LASTFM_API_KEY')
USER_AGENT = 'Dataquest'

headers = {
    'user-agent': USER_AGENT
}

payload = {
    'api_key': API_KEY,
    'method': 'chart.gettopartists',
    'format': 'json'
}

r = requests.get('http://ws.audioscrobbler.com/2.0/',
                 headers=headers, params=payload)
print(r.status_code)
