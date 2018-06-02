#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from pprint import pprint
import json




def raw_response(targetURL):
    targetURL = 'http://nixni.cc'
    response = requests.get(targetURL)
    # pprint(response.headers)
    a=json.dumps(dict(response.headers),indent=4, sort_keys=True)
    # print(a) 
    return a


# raw_response("http://nixni.cc")












# r = {'is_claimed': 'True', 'rating': 3.5}
# r = json.dumps(r)
# loaded_r = json.loads(r)
# loaded_r['rating'] #Output 3.5
# type(r) #Output str
# type(loaded_r) #Output dict