from django.db import models
from login.models import UserInfo


# 调整研学的表
class AdjustInf(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    ini_day = models.DateField('发起日期')
    be_day = models.DateField('被调整日期')
    day = models.DateField('调整日期')
    adjust_time = models.CharField('被调整研学时间', max_length=100)
    be_adjust_time = models.CharField('调整后研学时间', max_length=100)
    reason = models.TextField()
