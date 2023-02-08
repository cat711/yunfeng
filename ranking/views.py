from leave.models import LeaveInf
from login.models import UserInfo
import datetime as dt
from django.db.models import Count
from django.http import HttpResponse, JsonResponse
# Create your views here.


def rank_show(request):
    # uuid = request.session['id']
    uuid = 'admin_id'
    if uuid == 'admin_id':
        try:
            if request.method == 'GET':  # 获取时间
                s_date = request.GET.get('s_date')
                e_date = request.GET.get('e_date')
                date1 = dt.datetime.strptime(s_date, '%Y-%m-%d').date()
                date2 = dt.datetime.strptime(e_date, '%Y-%m-%d').date()
                users = LeaveInf.objects.filter(day__gte=date1, day__lte=date2).values('user_id')
                count_num = list(users.annotate(num=Count('user_id')))
                data = {}
                for i in count_num:  # 构造json
                    uid = i['user_id']
                    res = UserInfo.objects.get(id=uid).user_name
                    num = i['num']
                    data[res] = num
                sort_list = sorted(data.items(), key=lambda x: x[1])
                sort_data = []
                for i in range(len(sort_list)-1, -1, -1):  # 排序
                    user_count = {'name': sort_list[i][0], 'count': sort_list[i][1]}
                    sort_data.append(user_count)
                return_json = {'data': sort_data}
                result = JsonResponse(return_json)
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
    else:
        result = HttpResponse("请先登录")
        result["Access-Control-Allow-Origin"] = "*"
        result["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        result["Access-Control-Max-Age"] = "1000"
        return result
