from _aws import dynamodb
import datetime


# Declare params checker
global TABLENAME
global CURDATE
global PARAMS

# [ PARAMS FORMAT ]
# {
#     '<route-name>' : {
#         'method' : 'GET' | 'POST',
#         'function' : '<function to execute>',
#         'params' : [<params list>]
#     }
# }


TABLENAME = ''
CURDATE = str(datetime.datetime.now()).replace(' ','T')
PARAMS = {}







