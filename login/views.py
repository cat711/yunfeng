from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from login import models


def user_login(request):
    uid = request.POST.get('id')  # 用户名
    password = request.POST.get('password')  # 密码
    try:
        user = models.UserInfo.objects.get(id=uid)
    except:
        result = JsonResponse({'id': 0, "pw": 0})
        result["Access-Control-Allow-Origin"] = "*"
        result["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        result["Access-Control-Max-Age"] = "1000"
        return result
    if password == user.password:
        request.session['id'] = user.id
        result = JsonResponse({'id': 1, "pw": 1})
        result["Access-Control-Allow-Origin"] = "*"
        result["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        result["Access-Control-Max-Age"] = "1000"
        return result
    else:
        result = JsonResponse({'id': 1, "pw": 0})
        result["Access-Control-Allow-Origin"] = "*"
        result["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        result["Access-Control-Max-Age"] = "1000"
        return result
