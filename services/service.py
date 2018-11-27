

# Validate Query Params
def _validate(params,route,querystring,payload):
    _params = params[route]['params']
    if(params[route]['method']=='GET'):
        _toEval = querystring

    if(params[route]['method']=='POST'):
        _toEval = payload

    for param in _params:
        if( param not in _toEval):
            return 0
    return 1


# Execute Service Function
def _exe(service,route,querystring,body):
    service = __import__("services."+service,fromlist=[service])

    # Validate Required Params
    if(not _validate(service.PARAMS,route,querystring,body)):
        return {
            'status' : 400
        }

    return service._exe(route,querystring,body)

    




