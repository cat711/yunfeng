from login.models import UserInfo
from register.models import YunDingInfo
from django.http import HttpResponse
import json

# 邀请码
CODE = '1111'
# 邀请码长度
CODE_LEN = 4


def register(request):
    try:
        if request.method == 'POST':
            user_id = request.POST.get('user_id')
            invitation_code = request.POST.get('invitation_code')
            user_name = request.POST.get('user_name')
            direction = request.POST.get('direction')
            phase_num = request.POST.get('phase_num')
            password = request.POST.get('password')
            if not YunDingInfo.objects.filter(id=user_id, user_name=user_name).first():
                return HttpResponse(json.dumps({'result': 0, 'msg': "不在云顶书院"}))
            elif invitation_code != CODE:
                return HttpResponse(json.dumps({'result': 0, 'msg': "邀请码错误"}))
                # 判断学号ID是否重复
            elif UserInfo.objects.filter(id=user_id).first():
                return HttpResponse(json.dumps({'result': 0, 'msg': "用户已存在"}))
            elif len(user_id) != 10:
                return HttpResponse(json.dumps({'result': 0, 'msg': "学号为10位数字！"}))
            else:
                UserInfo.objects.create(id=user_id, user_name=user_name, phase_num=phase_num, direction=direction,
                                        password=password)
                return HttpResponse(json.dumps({'result': 1, 'msg': "创建成功"}))
    except:
        return HttpResponse("加载失败")
