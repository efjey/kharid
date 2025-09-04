from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt 
from web.models import *
from datetime import datetime

@csrf_exempt
def submit_expense(request):
    '''user submit the request and expense'''
    #TODO: validate data. user, token and amount might be fake
    if 'token' in request.POST:
        this_token = request.POST['token']
    else:
        this_token = None
    
    now = datetime.datetime.now()
    this_user = User.objects.filter(token__token = this_token).get()
    Expense.objects.create(user= this_user, amount= request.POST['amount'],
                            text = request.POST['text'], date=now)
    

    return JsonResponse({
        'status' : 'OK',
        
    }, encoder=JSONEncoder)