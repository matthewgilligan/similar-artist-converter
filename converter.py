import json
import os
import requests
import requests_cache
import time

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

results = []

page = 1
total_pages = 99999

while page <= total_pages:
  payload = {
      'method': 'chart.gettopartists',
      'limit': 500,
      'page': page
  }

  print("Requesting page {}/{}".format(page, total_pages))
  clear_output(wait=True)

  response = lastfm_get(payload)

  if response.status_code != 200:
    print(response.text)
    break

  page = int(response.json()['artists']['@attr']['page'])
  total_page = int(response.json()['artists']['@attr']['totalPages'])

  responses.append(response)

  if not getattr(response, 'from_cache', False):
    time.sleep(0.25)

  page += 1
