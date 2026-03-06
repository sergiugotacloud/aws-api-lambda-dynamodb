import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorLogs')

def lambda_handler(event, context):

    visitor_id = str(uuid.uuid4())

    table.put_item(
        Item={
            'visitorId': visitor_id,
            'timestamp': datetime.utcnow().isoformat()
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Visitor stored successfully')
    }
