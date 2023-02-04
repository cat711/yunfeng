from django.db import models
from register.models import UserInfo

# Create your models here.
class LeaveInfo(models.Model):
    ini_day = models.DateField('发起时间')
    day = models.DateField('请假的日期')
    time = models.CharField('研学时间', max_length=100)
    reason = models.TextField('原因')
    user = models.user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)


class UserInfo(models.Model):
    id = models.IntegerField('学号', primary_key=True)
    user_name = models.CharField('姓名', max_length=200)
    phase_num = models.CharField('期数', max_length=200)
    direction = models.CharField('方向', max_length=200)
    password = models.CharField('密码', max_length=200)
