# System default setting json loader

import json

global SETTINGS
SETTINGS = json.loads(open('util/settings.json').read())

# Get json setting by key
def _value(key):
    global SETTINGS
    return SETTINGS[key]

# Update setting value
def _update(key,value):
    global SETTINGS
    SETTINGS[key] = value
    jsonstring = json.dumps(SETTINGS,indent=4)
    fwriter = open('util/settings.json','w')
    fwriter.write(jsonstring)
    fwriter.close()




