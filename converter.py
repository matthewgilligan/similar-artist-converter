import json
import os
import requests

API_KEY = os.environ.get('LASTFM_API_KEY')
USER_AGENT = 'Dataquest'


def lastfm_get(payload):
  headers = {'user-agent': USER_AGENT}
  url = "http://ws.audioscrobbler.com/2.0/"

  payload['api_key'] = API_KEY
  payload['format'] = 'json'

  response = requests.get(url, headers=headers, params=payload)
  return response


def jprint(obj):
  text = json.dumps(obj, sort_keys=True, indent=4)
  print(text)


r = lastfm_get({'method': 'chart.gettopartists'})
print(r.status_code)

jprint(r.json()['artists']['@attr'])
