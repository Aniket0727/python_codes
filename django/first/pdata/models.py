from django.db import models

# Create your models here.

class pdata2(models.Model):
    oname=models.CharField(max_length=100)
    pname=models.CharField(max_length=100)
    page=models.CharField(max_length=100)
    op=models.IntegerField()
    sp=models.IntegerField()
    pd=models.TextField()
    address=models.TextField()
    image=models.FileField(upload_to="img/",max_length=250,null=True,default=None)
    uid=models.CharField(max_length=100,null=True,default=None)
    pid = models.AutoField(primary_key=True)

    def __str__(self):
        return self.pname