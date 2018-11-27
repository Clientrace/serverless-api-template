import os
import json
import boto3

# Initialize AWS Controllers
global DYNAMODB
global LAMBDA
global IAM

DYNAMODB = boto3.client('dynamodb')
LAMBDA = boto3.client('lambda')
IAM_client = boto3.client('iam')
IAM_res = boto3.resource('iam')
    


# Create Dynamodb Table
def _create_table(tablename,indexName):
    global DYNAMODB

    DYNAMODB.create_table(
        AttributeDefinitions = [
            {
                'AttributeName' : indexName,
                'AttributeType' : 'S'
            }
        ],
        ProvisionedThroughput = {
            'ReadCapacityUnits' : 5,
            'WriteCapacityUnits' : 5
        },
        TableName = tablename,
        KeySchema = [
            {
                'AttributeName' : indexName,
                'KeyType' : 'HASH'
            }
        ]
    )


# Load Local Policy Document
def load_iam_policies():
    roles = {}
    for json_file in os.listdir('iam_policy'):
        policy = open('iam_policy/'+json_file).read()
        policy_name = json_file.split('.')[0]
        roles[policy_name] = policy

    return roles


# AWS IAM Role Configuration
def _get_iam_role():
    global IAM_res
    global IAM_client

    try:
        response = IAM_client.create_role(
            RoleName = 'serverless-api',
            AssumeRolePolicyDocument = json.dumps({
                "Version" : "2012-10-17",
                "Statement" : [
                    {
                        "Effect" : "Allow",
                        "Principal" : {
                            "Service" : "lambda.amazonaws.com"
                        },
                        "Action" : ["sts:AssumeRole"]
                    }
                ]
            })
        )
        print('==> Role created')
    except Exception as e:
        # Role resource Name already exist
        if('(EntityAlreadyExists)' in str(e)):
            print('==> Role created')
        else:
            print('Something went wrong.')
            print(str(e))

    # attach policies
    roles = load_iam_policies()



    

# Create AWS Lambda Function
def _create_function(funcName):
    global LAMBDA

    # Compress This Directory
    file_name = 'zf.zip',
    cli_zip_cmd = 'zip -r '+file_name+' * -x .git/ .vscode/ @'
    zipFile = open('zf.zip','rb').read()

    response = LAMBDA.create_function(
        FunctionName = funcName,
        Runtime = 'python3.6',
        Role = ''
    )



_get_iam_role()











