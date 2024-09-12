from django.db import models

# Create your models here.
class Student(models.Model):
    firstname=models.CharField(max_length=200,blank=True,null=True)
    lastname=models.CharField(max_length=200,blank=True,null=True)
    
    def __str__(self):
        return self.firstname