from django.db import models

# Create your models here.
class customerdetail(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    avail_bal=models.IntegerField()
class transectiondetail(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    deb_amt=models.IntegerField()
    cr_amt=models.IntegerField()
    ac_bal=models.IntegerField()




