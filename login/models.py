from django.db import models

# Create your models here.
class UserInfo(models.Model):
    id = models.IntegerField('学号',primary_key=True)
    user_name = models.CharField('姓名',max_length=200)
    phase_num = models.CharField('期数', max_length=200)
    direction = models.CharField('方向', max_length=200)
    password = models.CharField('密码', max_length=200)