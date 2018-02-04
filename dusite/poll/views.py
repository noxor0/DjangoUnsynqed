from django.shortcuts import render
from . import models

def poll(request):
    poll_values = models.get_poll_values()
    return render(request, 'poll/poll_page.html', poll_values)

def poll_response(request, response):
    response_dict = models.put_vote_aws(response)
    return render(request, 'poll/poll_response.html', response_dict)

# '''
# I'm fairly sure theres a cleaner way to do this, but i dont know how to take
# the url of the vote response, and push it into a function here.
#
# JK I DID IT
# '''
# def poll_no(request):
#     return render(request, 'poll/poll_response.html', {'response': 'no'})
#
# def poll_yes(request):
#     return render(request, 'poll/poll_response.html', {'response': 'yes'})
#
# def poll_maybe(request):
#     return render(request, 'poll/poll_response.html', {'response': 'maybe'})
