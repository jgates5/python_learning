"""
type python

import request
import pprint

r = requests.get('https://api.dailysmarty.com/posts')
to see what the json will look like then use the variable then use the request def funcname(self, parameter_list):
r.json()
call pprint.pprint(r.json())
"""
#what to do with the data
"""
call pprint.pprint(r.json()['posts'][0]['url_for_post'])
