import traceback
from util import config
from services import service
from util import dynamoparser



# Main API Execution Point
def _exe(event,context):
    # Log Event
    print(event)

    body = event['body']
    path = event['params']['path']
    header = event['params']['header']
    querystring = event['params']['querystring']

    # Service Rerturn Data
    retData = service._exe(path['service'],path['path'],headers,querystring,body)

    # Parse Dynamo List Return
    if(type(retData).__name__=='list'):
        parsedList = []
        for data in retData:
            parsedList.append(
                dynamoparser.parse(data)
            )
        return parsedList

    # Parse Dynamod Dictionary Return 
    if(type(retData).__name__=='dict'):
        return dynamoparser.parse(retData)

    return dynamoparser.parse(retData)


# Lambda Execution Point
def lambda_handler(event,context):
    try:
        return _exe(event,context)
    except Exception as e:
        print(e)
        traceback.print_exc()
    return {
        'status' : 500,
        'description' : 'Internal Server Error'
    }


    