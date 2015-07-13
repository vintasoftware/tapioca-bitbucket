"""
Takes as it's input api.json that can be downloaded from:
https://api.apigee.com/v1/users/bitbucket/consoles/bitbucket/apidescription?format=internal
"""

import json
import re

api = json.loads(open('api.json').read())
apiv2 = api['application']['endpoints'][1]['resources']

resources = {}
uniq_id = 0


def longest_common_prefix(seq1, seq2):
    start = 0
    while start < min(len(seq1), len(seq2)):
        if seq1[start] != seq2[start]:
            break
        start += 1

    return seq1[:start]


def longest_common_suffix(seq1, seq2):
    return longest_common_prefix(seq1[::-1], seq2[::-1])[::-1]


def longest_common_str(seq1=None, seq2=None):
    global uniq_id
    if not seq2 and seq1:
        return seq1
    if not seq1:
        uniq_id += 1
        return 'noname_%i' % uniq_id
    a = longest_common_prefix(seq1, seq2)
    b = longest_common_suffix(seq1, seq2)
    if not a and not b:
        uniq_id += 1
        return 'noname_%i' % uniq_id
    return a if len(a) > len(b) else b


def convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def get_or_create_mutable_value_from_dict(dictionary, name, ttype):
    mutable = dictionary.get(name, ttype())
    dictionary[name] = mutable
    return mutable


for method in apiv2:
    method_dict = get_or_create_mutable_value_from_dict(resources,
                                                        method['path'].rstrip('/'),
                                                        dict)
    docs_list = get_or_create_mutable_value_from_dict(method_dict,
                                                      'docs',
                                                      list)
    if 'doc' in method['method'] and method['method']['doc']['content'] != 'TBD':
        docs_list.append(method['method']['doc']['apigee:url'])

    http_methods = get_or_create_mutable_value_from_dict(method_dict,
                                                         'http_methods',
                                                         list)
    http_methods.append(method['method']['name'])

    ids = get_or_create_mutable_value_from_dict(method_dict,
                                                'ids',
                                                list)
    ids.append(method['method']['id'])

final_resources = {}
for path, resource in resources.items():
    resource['id'] = longest_common_str(*(resource['ids'][0:2]))
    d = {}
    d['resource'] = path
    final_resources[convert(resource['id'])] = d

    d['methods'] = list(set(resource['http_methods']))
    d['docs'] = (resource['docs'][0] if resource['docs'] else
                 'https://confluence.atlassian.com/display/BITBUCKET/Version+2')

print json.dumps(final_resources)
