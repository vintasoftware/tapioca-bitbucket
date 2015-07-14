# coding: utf-8

from tapioca import (
    TapiocaAdapter, generate_wrapper_from_adapter)
from requests_oauthlib import OAuth2

from resource_mapping import RESOURCE_MAPPING


class BitbucketClientAdapter(TapiocaAdapter):
    api_root = 'https://api.bitbucket.org/2.0'
    resource_mapping = RESOURCE_MAPPING

    def get_request_kwargs(self, api_params):
        client_id = api_params.get('client_id')
        return {
            'auth': OAuth2(client_id,
                token={
                    'access_token': api_params.get('access_token'),
                    'token_type': 'Bearer'}),
            'headers': {'Content-Type': 'application/json'}
        }

    def get_iterator_list(self, response_data):
        return response_data['values']

    def get_iterator_next_request_kwargs(self,
            iterator_request_kwargs, response_data, response):
        page = response_data.get('page')
        if not page:
            return

        url = response_data.get('next')

        if url:
            return {'url': url}


Bitbucket = generate_wrapper_from_adapter(BitbucketClientAdapter)
