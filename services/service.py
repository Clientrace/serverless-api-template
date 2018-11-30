

# Validate Query Params
def _validate(reqParams,method,querystring,payload):
    if(method == 'GET'):
        _toEval = querystring
    if(method == 'POST'):
        _toEval = payload

    for param in reqParams:
        if( param not in _toEval):
            return 0

    return 1


# Execute Service Function
def _exe(service,route,querystring,body):
    # Get API Service
    service = __import__("services."+service,fromlist=[service])

    # Check if route exists
    if(route not in service.PARAMS):
        return {
            'status' : 405,
            'description' : 'Method not allowed'
        }

    # Service Function
    service_func = service.PARAMS[route]['function']
    service_method = service.PARAMS[route]['method']
    serivce_params = service.PARAMS[route]['params']


    # Validate Required Params
    if(not _validate(service_params,service_method,querystring,body)):
        return {
            'status' : 400,
            'description' : 'Incomplete Params'
        }


    # Execute Service
    service_exe = getattr(service,service_func)
    if(service_method == 'GET'):
        return service_exe(querystring)

    if(service_method == 'POST'):
        return service_exe(body)


    return {
        'status' : 405,
        'description' : 'Method not allowed'
    }




    