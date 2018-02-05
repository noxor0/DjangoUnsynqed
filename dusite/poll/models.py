from django.db import models
import requests
import json
import os

#Extract this?
aws_url = os.environ['AWSURL']
header = {'x-api-key': os.environ['AWSAPIKEY']}

def get_counts_aws():
    '''
    Queries the GET API that scans the table for the count of the responses.
    If aws get query fails, all bars will just be full. For the purpose of this
    project, handling it this way should be fine.
    :return: A dictionary that includes the counts of each response and total.
    '''
    query_params = '?TableName=poll_table'
    r = requests.get(aws_url + query_params, headers=header)
    dynamo_return = json.loads(r.text)
    return_dict = {}
    total = 0
    if dynamo_return['ResponseMetadata']['HTTPStatusCode'] != 200:
        return_dict['total'] = 1
        for item in ['yes', 'no', maybe]:
            return_dict[item] = 1

    for item in dynamo_return['Items']:
        return_dict[item['option']['S']] = int(item['count']['N'])
        total += int(item['count']['N'])
    return_dict['total'] = total

    return return_dict

def get_poll_values():
    '''
    Gets the poll percentage values and returns them in a dictionary that has each
    response and their percent of the total votes.

    :return: A dictionary that includes the response and its percentage
    '''
    counts_dict = get_counts_aws()
    total = 0
    percent_dict = {}
    for key in counts_dict:
        if key is not 'total':
            percent_dict[key] = int(counts_dict[key] / counts_dict['total'] * 100)
    return percent_dict

def put_vote_aws(response):
    '''
    Adds an additional count to the DB to the response selected by the user.
    Incorrect responses will be rejected and an user will be notified.
    Requests will add one to the count through the PUT API on AWS.
    Have some simple error handling if response code isnt 200. Will handle the
    exception gracefully on the frontend with an error message.

    :param response: the response selected by the user to be incremented by 1
    :returns: A dictionary with a the accept response that was returned from AWS,
    and flavor text for delivery.
    '''
    response_dict = {}
    acceptable_responses = ['yes', 'no', 'maybe']
    if response not in acceptable_responses:
        response_dict['response'] = 'Not an acceptable response!'
        response_dict['flavor_line'] = 'Looks like something went wrong!'
        return response_dict

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

    r = requests.put(aws_url, data=json.dumps(body_dict), headers=header)
    response_json = json.loads(r.text)

    if response_json['ResponseMetadata']['HTTPStatusCode'] == 200:
        response_dict['response'] = response
        response_dict['flavor_line'] = 'Thank you for voting! You voted:'
    else:
        response_dict['response'] = "Something went wrong with AWS!"

    return response_dict
