# Get Lambda Config
import boto3
from util import settings


global LAMBDA
global FUNCTIONAME

FUNCTIONAME = settings._value('function_name')
LAMBDA = boto3.client('lambda')


# Get AWS Lambda Environment Vars
def env_variables():
    global LAMBDA
    global FUNCTIONAME

    functionConfig = LAMBDA.get_function(FunctionName=FUNCTIONAME)
    keys = functionConfig['Configuration']['Environment']['Variables']

    return keys



