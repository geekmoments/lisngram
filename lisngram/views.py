'''VIEWS module'''

#django
from django.http import HttpResponse

#utilities
from datetime import datetime
import json


def hello_world(request):
    now = datetime.now().strftime('%b %dth,%Y - %H:%M hrs')

    return HttpResponse('Hello,Lisn users, server time is {now}'.format(now=now))

def sorted_int(request):

    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_nb = sorted(numbers)
    #import pdb; pdb.set_trace()
    data = {
        'status':'ok',
        'numbers': sorted_nb,
        'message': 'instegrated sorted successfully.'

    }
    return HttpResponse(
        json.dumps(data,indent=2),
        content_type='application/json')

def say_hi(request,name,age):

    if age < 12 :
        message = 'Sorry {},you are no allowed here'.format(name)
    else:
        message = 'Hello,{}! Welcome to LISNgram'.format(name)
    
    return HttpResponse(message)



