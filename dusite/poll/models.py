from django.db import models
import requests
import json

#Extract this?
aws_url = 'https://umwvdt8m7i.execute-api.us-west-2.amazonaws.com/prod/poll_handler'

def get_counts_aws():
    query_params = '?TableName=poll_table'
    r = requests.get(aws_url + query_params)
    dynamo_return = json.loads(r.text)
    return_dict = {}
    total = 0
    for item in dynamo_return['Items']:
        return_dict[item['option']['S']] = int(item['count']['N'])
        total += int(item['count']['N'])
    return_dict['total'] = total
    return return_dict

def get_poll_values():
    counts_dict = get_counts_aws()
    total = 0
    percent_dict = {}
    for key in counts_dict:
        if key is not 'total':
            percent_dict[key] = int(counts_dict[key] / counts_dict['total'] * 100)
    return percent_dict

def put_vote_aws(response):
    body_dict = {
        "TableName":"poll_table",
        "Key":{"option": {"S": response}},
        "AttributeUpdates" : {
            "count": {
                "Action": "ADD",
                "Value": {"N":"1"}
            }
        }
    }

    r = requests.put(aws_url, data=json.dumps(body_dict))

    response_json = json.loads(r.text)
    success = response if response_json['ResponseMetadata']['HTTPStatusCode'] == 200 else "Something went wrong!"
    return success
