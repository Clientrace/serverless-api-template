# Get Latest Cloudwatch Log

import os
import boto3
from util import settings

global LOGS
LOGS = boto3.client(
    'logs'
)


# Get Cloudwatch Stream Name
def get_stream_name(groupName):
    global LOGS

    resp = LOGS.describe_log_streams(
        logGroupName = groupName,
        orderBy = 'LastEventTime',
        descending = True,
        limit = 2
    )
    return resp['logStreams'][0]['logStreamName']


# Get Log Stream Data
def get_log_stream(groupName):
    global LOGS

    streamName = get_stream_name(groupName)
    resp = LOGS.get_log_events(
        logGroupName = groupName,
        logStreamName = streamName
    )

    return resp['events']


if __name__ == '__main__':
    functionName = settings._value('function_name')
    streams = get_log_stream('/aws/lambda/'+functionName)
    for stream in streams:
        print(stream['message']+'\n')


    



