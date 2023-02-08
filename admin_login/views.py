from django.http import JsonResponse
from admin_login import models


def admin_login(request):
    admin_id = request.POST.get('admin_id')  # 用户名
    password = request.POST.get('password')  # 密码
    try:
        admin = models.AdminInfo.objects.get(admin_id=admin_id)
    except:
        date = {'result': 1, "msg": "用户名错误"}
        result = JsonResponse({'request': date})
        result["Access-Control-Allow-Origin"] = "*"
        result["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        result["Access-Control-Max-Age"] = "1000"
        return result
    if password == admin.password:
        date_msg = "登陆成功"
        date_code = 0
        request.session['id'] = 'admin_id'
    else:
        date_msg = "密码输入错误"
        date_code = 1
    date = {'result': date_code, 'msg': date_msg}

    result = JsonResponse({date})
    result["Access-Control-Allow-Origin"] = "*"
    result["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    result["Access-Control-Max-Age"] = "1000"
    return result
