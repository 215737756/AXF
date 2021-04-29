from django.db import models


# Create your models here.
class AxfUser(models.Model):
    username = models.CharField(max_length=32)
    account = models.CharField(max_length=32)
    password = models.CharField(max_length=32,default='')
    email = models.CharField(max_length=32)
    icon = models.ImageField()

    class Meta:
        db_table = 'axfuser'


