from django.db import models

def get_counts_aws():
    # Should call api gateway url here
    # get the values from the DB
    # return %
    return {'yes': 4, 'maybe': 2, 'no': 0, 'total':6}

def get_poll_values():
    counts_dict = get_counts_aws()
    total = 0
    percent_dict = {}
    for key in counts_dict:
        if key is not 'total':
            percent_dict[key] = int(counts_dict[key] / counts_dict['total'] * 100)
    return percent_dict
