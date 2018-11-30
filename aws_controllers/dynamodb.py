import boto3

global DYNAMODB

DYNAMODB = boto3.client(
    'dynamodb'
)

# Add Table Item
def put_item(tableName,item):
    global DYNAMODB

    response = DYNAMODB.put_item(
        TableName = tableName,
        Item = item,
        ReturnConsumedCapacity = 'TOTAL'
    )

    return response

# Update Table Item
def update_item(tableName,key,item):
    global DYNAMODB

    response = DYNAMODB.update_item(
        TableName = tableName,
        Key = key,
        AttributeUpdates = item
    )

    return response

# Increment Item Attribute Count
def increment_item_value(tableName,key,attribNum):
    global DYNAMODB

    response = DYNAMODB.update_item(
        TableName = tableName,
        Key = key,
        UpdateExpression = 'ADD #'+attribNum+' :inc',
        ExpressionAttributeValues = {
            ':inc' : {
                'N' : '1'
            }
        },
        ExpressionAttributeNames = {
            '#'+attribNum : attribNum
        },
        ReturnValues = 'UPDATE_NEW'
    )

    return response

# Update item value
def update_item(tableName,key,item):
    global DYNAMODB

    response = DYNAMODB.update_item(
        TableName = tableName,
        Key = key,
        AttributeUpdates = item
    )

    return response

# Get item by primary key
def get_item(tableName,key):
    global DYNAMODB

    response = DYNAMODB.get_item(
        TableName = tableName,
        Key = key
    )

    return response

# Delete Dynamodb Item
def delete_item(tableName,key):
    global DYNAMODB

    response = DYNAMODB.delete_item(
        TableName = tableName,
        Key = key
    )

    return response 

# Query db item
def query(tableName,indexName,filterExp,expAttrbNames,expAttrbValues,limit,exclusiveStartKey=None):
    global DYNAMODB

    if(exclusiveStartKey):
        response = DYNAMODB.query(
            TableName = tableName,
            IndexName = indexName,
            Limit = limit,
            ExclusiveStartKey = exclusiveStartKey,
            Select = 'ALL_ATTRIBUTES',
            KeyConditionExpression = filterExp,
            ExpressionAttributeNames = expAttrbNames,
            ExpressionAttributeValues = expAttrbValues
        )
    else:
        response = DYNAMODB.query(
            TableName = tableName,
            IndexName = indexName,
            Limit = limit,
            Select = 'ALL_ATTRIBUTES',
            KeyConditionExpression = filterExp,
            ExpressionAttributeNames = expAttrbNames,
            ExpressionAttributeValues = expAttrbValues
        )

    return response

# Get All Table Items
def scan_all(tableName):
    global DYNAMODB

    paginator = DYNAMODB.get_paginator('scan')
    filterExp = {
        'TableName' : tableName,
        'Limit' : 5
    }


