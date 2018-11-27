from services import service
from util import config



# Main API Execution Point
def lambda_handler(event,context):
    # Log Event
    print(event)

    body = event['body']
    path = event['params']['path']
    header = event['params']['header']
    querystring = event['params']['querystring']










