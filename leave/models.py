from django.db import models
from register.models import UserInfo
# Create your models here.


class LeaveInf(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    ini_day = models.DateField('发起日期')
    day = models.DateField()
    time = models.CharField('时间', max_length=100)
    reason = models.TextField()


