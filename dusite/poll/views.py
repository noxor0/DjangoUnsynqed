from django.shortcuts import render
from . import models

def poll(request):
    poll_values = models.get_poll_values()
    return render(request, 'poll/poll_page.html', poll_values)

def poll_response(request, response):
    response_dict = models.put_vote_aws(response)
    return render(request, 'poll/poll_response.html', response_dict)
