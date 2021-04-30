from django.db import models


# Create your models here.
class AxfUser(models.Model):
    username = models.CharField(max_length=32)
    account = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    icon = models.ImageField()
    activate = models.BooleanField(default=False)
    token = models.CharField(max_length=64)

    class Meta:
        db_table = 'axfuser'
