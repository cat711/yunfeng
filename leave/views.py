from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from leave.models import LeaveInf
from login.models import UserInfo
import datetime as dt


# 新请假
def create_leave(request):
    try:
        if request.method == 'POST':
            # uid = request.POST.get('id')
            uid = request.session['id']
            date = request.POST.get('date')
            time = request.POST.get('time')
            reason = request.POST.get('reason')
            ini_date = request.POST.get('ini_date')
        LeaveInf.objects.create(user_id=uid, day=date, time=time, reason=reason, ini_day=ini_date)
        return HttpResponse(json.dumps({'result': '1'}))
    except:
        return HttpResponse(json.dumps({'result': '0'}))


def user_exit(request):  # 未使用
    del request.session['id']
    return HttpResponse('退出成功')


# 请假信息显示
def leave_show(request):
    try:
        if request.method == 'GET':
            s_date = request.GET.get('s_date')
            e_date = request.GET.get('e_date')
            uuid = request.session['id']
            date1 = dt.datetime.strptime(s_date, '%Y-%m-%d').date()
            date2 = dt.datetime.strptime(e_date, '%Y-%m-%d').date()
            re_inf = {}
            users = LeaveInf.objects.filter(user_id=uuid, ini_day__gte=date1, ini_day__lte=date2).order_by(
                'ini_day').values('ini_day', 'day', 'time', 'reason')
            re_inf["data"] = list(users)
            re_inf['counts'] = len(re_inf['data'])
        return JsonResponse(re_inf)
    except:
        return HttpResponse("加载失败")
