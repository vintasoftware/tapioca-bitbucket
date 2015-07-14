
import sys
import webbrowser

from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth

from decouple import config

# Add a .env file with CONSUMER_KEY and CONSUMER_SECRETE
# variables in the same folder as this file.
CONSUMER_KEY = config('CONSUMER_KEY')
CONSUMER_SECRETE = config('CONSUMER_SECRETE')


def authenticate():
    bitbucket = OAuth2Session(CONSUMER_KEY)

    authorization_url, state = bitbucket.authorization_url(
        'https://bitbucket.org/site/oauth2/authorize')
    webbrowser.open(authorization_url)


def get_auth_token(code):
    bitbucket = OAuth2Session(CONSUMER_KEY)
    response = bitbucket.fetch_token(
        'https://bitbucket.org/site/oauth2/access_token',
        auth=HTTPBasicAuth(CONSUMER_KEY, CONSUMER_SECRETE),
        code=code
        )
    print('access_token:  ' + response['access_token'])
    print('refresh_token: ' + response['refresh_token'])
    print('scopes:        ' + response['scopes'])
    print('token_type:    ' + response['token_type'])


if __name__ == '__main__':
    if sys.argv[1] == 'auth':
        authenticate()
    elif sys.argv[1] == 'token':
        get_auth_token(sys.argv[2])
