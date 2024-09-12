from django.db import models

# Create your models here.

class mydata3(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    pass1=models.CharField(max_length=100)
    pass2=models.CharField(max_length=100)
    


