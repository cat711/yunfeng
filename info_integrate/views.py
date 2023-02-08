from django.shortcuts import render

# Create your views here.
import datetime as dt
from django.http import JsonResponse, HttpResponse
from leave import models
from login.models import UserInfo
from adjust.models import AdjustInf


# Create your views here.
def info_integrate(request):
    try:
        if request.method == 'GET':
            # if request.session['id'] == 'admin_id':  # session验证
            # now_day = datetime.date.today()
            i = 1
            if i == 1:
                day = request.GET.get('s_date')
                now_day = dt.datetime.strptime(day, '%Y-%m-%d').date()
                leave_inf = models.LeaveInf.objects.filter(day=now_day).values_list()
                res = []
                for i in leave_inf:
                    leave = {}
                    uid = i[1]
                    res_name = UserInfo.objects.get(id=uid).user_name
                    res_direction = UserInfo.objects.get(id=uid).direction
                    res_time = i[4]
                    res_reason = i[5]
                    leave['name'] = res_name
                    leave['direction'] = res_direction
                    leave['time'] = res_time
                    leave['reason'] = res_reason
                    res.append(leave)
                # 调研学显示
                adjust_inf = AdjustInf.objects.filter(be_day=now_day).values_list()
                print(adjust_inf)
                resa = []
                for i in adjust_inf:
                    adjust = {}
                    uid = i[1]
                    res_name = UserInfo.objects.get(id=uid).user_name
                    res_direction = UserInfo.objects.get(id=uid).direction
                    res_time = i[6]
                    res_reason = i[7]
                    adjust['name'] = res_name
                    adjust['direction'] = res_direction
                    adjust['time'] = res_time
                    adjust['reason'] = res_reason
                    resa.append(adjust)
                data = {'leave': res, 'adjust': resa}
                result = JsonResponse(data)
                result["Access-Control-Allow-Origin"] = "*"
                result["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
                result["Access-Control-Max-Age"] = "1000"
                return result
    except:
        result = HttpResponse("加载失败")
        result["Access-Control-Allow-Origin"] = "*"
        result["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        result["Access-Control-Max-Age"] = "1000"
        return result
