from django.db import models


# Create your models here.
class Base_axf(models.Model):
    name = models.CharField(max_length=32)
    img = models.CharField(max_length=168)
    trackid = models.CharField(max_length=168)

    class Meta:
        abstract = True
        db_table = 'base_axf'


class Wheel(Base_axf):
    class Meta:
        db_table = 'axf_wheel'


class AxfTopMenu(Base_axf):
    class Meta:
        db_table = 'axf_topmenu'


class AxfMustBuy(Base_axf):
    class Meta:
        db_table = 'axf_mustbuy'


class AxfMainShow(Base_axf):
    categoryid = models.IntegerField()
    brandname = models.CharField(max_length=64)

    img1 = models.CharField(max_length=128)
    childcid1 =models.IntegerField()
    productid1 = models.IntegerField()
    longname1 = models.CharField(max_length=128)
    price1 = models.FloatField()
    marketprice1 = models.FloatField()

    img2 = models.CharField(max_length=128)
    childcid2 =models.IntegerField()
    productid2 = models.IntegerField()
    longname2 = models.CharField(max_length=128)
    price2 = models.FloatField()
    marketprice2 = models.FloatField()

    img3 = models.CharField(max_length=128)
    childcid3 =models.IntegerField()
    productid3 = models.IntegerField()
    longname3 = models.CharField(max_length=128)
    price3 = models.FloatField()
    marketprice3 = models.FloatField()

    class Meta:
        db_table = 'axf_mainshow'