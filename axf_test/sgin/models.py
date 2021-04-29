from django.db import models


# Create your models here.
class Test(models.Model):
    name = models.CharField(u'菜单', max_length=32)

    class Meta:
        db_table = 'test'

