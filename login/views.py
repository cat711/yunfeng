from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from login import models

def user_login(request):
    uid = request.POST.get('id')  # 用户名
    password = request.POST.get('password')  # 密码
    try:
        user = models.UserInfo.objects.get(id=uid)
    except:
        data = {'code': 1, "msg": "用户名错误"}
        return JsonResponse({'request': data})
    if password == user.password:
        data_msg = "登陆成功"
        data_code = 0
        request.session['id'] = user.id
    else:
        data_msg = "密码输入错误"
        data_code = 1
    data = {'code': data_code, 'msg': data_msg}

    return JsonResponse({'request': data})
