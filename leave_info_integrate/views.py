import datetime
import json
from django.shortcuts import HttpResponse, render
from leave_info_integrate import models


# Create your views here.
def leave_info_integrate(request):
    if request.method == 'GET':
        state = request.GET.get(key='state')
        if state:
            leave_data = {
                'name': [],
                'user_id': [],
                'time': [],
                'reason': []
            }
            now_day = datetime.date.today()
            leave_info = models.LeaveInfo.objects.filter(day=now_day).values_list()
            for info in leave_info:
                leave_data['name'].append(models.UserInfo.objects.filter(id=info[5]).values('user_name').get()['user_name'])
                leave_data['user_id'].append(info[5])
                leave_data['time'].append(info[3])
                leave_data['reason'].append(info[4])
            return HttpResponse(json.dumps(leave_data), content_type="application/json")
        else:
            return render(request, '管理登录页面.html')

