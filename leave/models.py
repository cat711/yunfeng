from django.db import models

# Create your models here.
class LeaveInf(models.Model):
    id = models.ForeignKey(to='user', to_field='id', on_delete=models.CASCADE)
    day = models.DateField()
