# System default setting json loader

import json

global SETTINGS
SETTINGS = json.loads(open('util/settings.json').read())

# Get json setting by key
def _value(key):
    global SETTINGS
    return SETTINGS[key]



