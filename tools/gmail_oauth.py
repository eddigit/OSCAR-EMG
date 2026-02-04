#!/usr/bin/env python3
import json
import urllib.parse

# Load credentials
with open('tools/gmail-credentials.json') as f:
    creds = json.load(f)['installed']

# Build OAuth URL
params = {
    'client_id': creds['client_id'],
    'redirect_uri': 'http://localhost',
    'response_type': 'code',
    'scope': 'https://www.googleapis.com/auth/gmail.readonly https://www.googleapis.com/auth/gmail.send',
    'access_type': 'offline',
    'prompt': 'consent'
}

auth_url = creds['auth_uri'] + '?' + urllib.parse.urlencode(params)
print("AUTH_URL:", auth_url)
