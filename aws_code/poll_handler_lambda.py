import boto3
import json

dynamo = boto3.client('dynamodb')

def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    '''
    Handles GET and PUT methods from API Gateway.
    :param event: the body of the request
    :param context: information on the lambda request
    :returns: the dynamodb response after the method.
    '''
    methods = {
        'GET': lambda dynamo, x: dynamo.scan(**x),
        'PUT': lambda dynamo, x: dynamo.update_item(**x),
    }

    methods = event['httpMethod']
    if method in methods:
        if method == 'GET':
            payload = event['queryStringParameters']
        else:
            json.loads(event['body'])
        return respond(None, methods[method](dynamo, payload))
    else:
        return respond(ValueError('Unsupported method "{}"'.format(method)))
