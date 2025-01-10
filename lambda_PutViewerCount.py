import boto3
from botocore.exceptions import ClientError
import json


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ViewCount')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        new_value = body['count']

        response = table.update_item(
            Key={
                'Count': new_value,
            },
            UpdateExpression='SET #count = :val',
            #Tells Dynamodb how to update the item. Set is the commmand to update or add attributes

            ExpressionAttributeNames={ #'#count' is a placeholder for the attribute name 'count'. We use "#"" because "count" is a 
            #reserved word in Dynamodb. The ExpressionAttributeNames map the key (the name that you want to use) and the value
            # is the attribute name you want to expand to
                '#V': 'Value',
            },
            ExpressionAttributeValues={
                ':val': new_value, #expression attribute values must always start with a colon and must always specify the type 
                #of the value being referenced.
            },
            ReturnValues='UPDATED_NEW'
        )
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'message': 'Value updated successfully',
                'new_value': new_value
            })
        }  
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'message': 'Error updating value',
                'error': str(e)
            })
        }

