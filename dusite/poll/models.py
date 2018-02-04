from django.db import models
import requests
import json

'''
{
    "TableName":"poll_table",
    "Key":{"option": {"S": "yes"}},
    "AttributeUpdates" : {
        "count": {
            "Action": "ADD",
            "Value": {"N":"1"}
        }

    }
}

'''

def get_counts_aws():
    # Should call api gateway url here
    r = requests.get('https://umwvdt8m7i.execute-api.us-west-2.amazonaws.com/prod/poll_handler?TableName=poll_table')
    # get the values from the DB
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
