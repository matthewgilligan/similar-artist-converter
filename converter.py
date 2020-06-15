import os
import requests

API_KEY = os.environ.get('LASTFM_API_KEY')
USER_AGENT = 'Dataquest'

headers = {
    'user-agent': 'Dataquest'
}

r = requests.get('http://my-api-ulr', headers=headers)
