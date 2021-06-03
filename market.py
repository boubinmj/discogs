#!/usr/bin/env python
#
# This illustrates the call-flow required to complete an OAuth request
# against the discogs.com API, using python3-discogs-client libary.
# The script will download and save a single image and perform and
# an API search API as an example. See README.md for further documentation.

import sys

import discogs_client
from discogs_client.exceptions import HTTPError
import csv
import pandas as pd

# Your consumer key and consumer secret generated and provided by Discogs.
# See http://www.discogs.com/settings/developers . These credentials
# are assigned by application and remain static for the lifetime of your discogs
# application. the consumer details below were generated for the
# 'discogs-oauth-example' application.
# NOTE: these keys are typically kept SECRET. I have requested these for
# demonstration purposes.

consumer_key = 'JJCOegYnRLCLRejtcZbo'
consumer_secret = 'UFlGrCViqSkoBNfRTGZyUfmpTGNbFbMM'

# A user-agent is required with Discogs API requests. Be sure to make your
# user-agent unique, or you may get a bad response.
user_agent = 'discogs_api_example/2.0'

# instantiate our discogs_client object.
discogsclient = discogs_client.Client(user_agent)

# prepare the client with our API consumer data.
discogsclient.set_consumer_key(consumer_key, consumer_secret)
token, secret, url = discogsclient.get_authorize_url()

print(' == Request Token == ')
print(f'    * oauth_token        = {token}')
print(f'    * oauth_token_secret = {secret}')
print()

# Prompt your user to "accept" the terms of your application. The application
# will act on behalf of their discogs.com account.
# If the user accepts, discogs displays a key to the user that is used for
# verification. The key is required in the 2nd phase of authentication.
print(f'Please browse to the following URL {url}')

accepted = 'n'
while accepted.lower() == 'n':
    print
    accepted = input(f'Have you authorized me at {url} [y/n] :')


# Waiting for user input. Here they must enter the verifier key that was
# provided at the unqiue URL generated above.
oauth_verifier = input('Verification code : ')

try:
    access_token, access_secret = discogsclient.get_access_token(oauth_verifier)
except HTTPError:
    print('Unable to authenticate.')
    sys.exit(1)

# fetch the identity object for the current logged in user.
user = discogsclient.identity()

print
print(' == User ==')
print(f'    * username           = {user.username}')
print(f'    * name               = {user.name}')
print(' == Access Token ==')
print(f'    * oauth_token        = {access_token}')
print(f'    * oauth_token_secret = {access_secret}')
print(' Authentication complete. Future requests will be signed with the above tokens.')

# With an active auth token, we're able to reuse the client object and request
# additional discogs authenticated endpoints, such as database search.


import urllib.request, json
import pandas as pd

url = "https://api.discogs.com/marketplace/listings/172723812" + '/' + oauth_verifier
response = urllib.request.urlopen(url)
data = json.loads(response.read())
# print(data.keys())
# print(type(data))

# print(type(data['releases']))

for entry in data:
	print(type(entry))

# for entry in data:
# 		print(entry)
# 		print('\n')
# 		print('\n')
