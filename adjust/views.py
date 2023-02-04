from django.shortcuts import render

# Create your views here.
import json
from django.http import HttpResponse, JsonResponse
from adjust.models import AdjustInf
import datetime as dt


# 新请假
# 调研学方法
def create_adjust(request):
    try:
        if request.method == 'POST':
            uid = request.session['id']
            day = request.POST.get('date')  # 调整后日期
            ini_date = request.POST.get('ini_date')  # 发起日期
            be_day = request.POST.get('be_date')  # 被调整日期
            adjust_time = request.POST.get('adjust_time')  # 调整后时间
            be_adjust_time = request.POST.get('be_adjust_time')  # 被调整时间
            reason = request.POST.get('reason')
        AdjustInf.objects.create(user_id=uid, day=day, be_day=be_day, ini_day=ini_date, adjust_time=adjust_time,
                                 be_adjust_time=be_adjust_time, reason=reason)
        return HttpResponse(json.dumps({'result': '1'}))
    except:
        return HttpResponse(json.dumps({'result': '0'}))

    # 信息提交


def adjust_query(request):
    # uu_id = request.COOKIES.values
    # uid = request.session['uu_id']
    uid = '2022007184'
    users = AdjustInf.objects.filter(user_id=uid)
    return HttpResponse(users.values())


def user_exit(request):
    del request.session['uu_id']
    return HttpResponse('退出成功')


def adjust_show(request):
    try:
        if request.method == 'GET':
            s_date = request.GET.get('s_date')  # 周一时间
            e_date = request.GET.get('e_date')  # 周日时间
            uuid = request.session['id']  # session
            date1 = dt.datetime.strptime(s_date, '%Y-%m-%d').date()  # 时间格式转化
            date2 = dt.datetime.strptime(e_date, '%Y-%m-%d').date()  # 时间格式转化
            re_inf = {}
            users = AdjustInf.objects.filter(user_id=uuid, ini_day__gte=date1, ini_day__lte=date2).order_by(
                'ini_day').values('day', 'ini_day', 'adjust_time', 'be_day', 'be_adjust_time', 'reason')
            re_inf["data"] = list(users)
            re_inf['counts'] = len(re_inf['data'])
        return JsonResponse(re_inf)
    except:
        return HttpResponse("加载失败")
