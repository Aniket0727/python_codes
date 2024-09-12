from django.db import models

# Create your models here.
class productclickscount(models.Model):
    uid=models.IntegerField(null=True)
    pid=models.IntegerField(null=True)
    pname=models.CharField(max_length=100)
    productclick=models.IntegerField(null=True)