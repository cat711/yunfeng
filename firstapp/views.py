from django.shortcuts import render
import json
from django.http import HttpResponse


# Create your views here.

def test_land(request):
    if request.method == 'GET':
        return HttpResponse("ok")
    user_id = ['2022007184']
    password = ['ycx666']
    if request.method == 'POST':
        test_name = request.POST.get('id')
        test_password = request.POST.get('pw')
        if test_name == user_id[0]:
            if test_password != password[0]:
                return HttpResponse(json.dumps({'user_id': '1', 'password': '0'}))
            if test_password == password[0]:
                return HttpResponse(json.dumps({'user_id': '1', 'password': '1'}))
        if test_password != user_id[0]:
            return HttpResponse(json.dumps({'user_id': '0', 'password': '0'}))
