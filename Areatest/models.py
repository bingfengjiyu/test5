from django.db import models

# Create your models here.


class AreaInfo(models.Model):
    atitle=models.CharField(max_length=20)
    aParent=models.ForeignKey('self',null=True,blank=True)


    class Meta():
        db_table="booktest_areainfo"