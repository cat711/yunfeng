from django.db import models


# Create your models here.
class AdminInfo(models.Model):
    admin_id = models.IntegerField('学号', primary_key=True)
    password = models.CharField('密码', max_length=200)
