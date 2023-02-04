from django.db import models


class YunDingInfo(models.Model):
    id = models.IntegerField('学号', primary_key=True)
    user_name = models.CharField('姓名', max_length=200)
