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

# Update Table Item
def update_item(tableName,key,item):
    global DYNAMODB

    response = DYNAMODB.update_item(
        TableName = tableName,
        Key = key,
        AttributeUpdates = item
    )









