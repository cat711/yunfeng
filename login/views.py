from django.shortcuts import render
from django.http import JsonResponse
from login import models

def user_login(request):
    id = request.POST.get('id')  # 用户名
    password = request.POST.get('password')  # 密码
    try:
        user = models.UserInfo.objects.get(id=id)
    except:
        date = {'code': 1, "msg": "用户名错误"}
        return JsonResponse({'request': date})
    if password == user.password:
        date_msg = "登陆成功"
        date_code = 0
        request.session['id'] = user.id
    else:
        date_msg = "密码输入错误"
        date_code = 1
    date = {'flag': date_code, 'msg': date_msg}

    return JsonResponse({'request': date})
