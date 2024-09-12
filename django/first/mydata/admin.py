from django.contrib import admin
from mydata.models import mydata3
# Register your models here.

class data(admin.ModelAdmin):
    list_display=('name','username','pass1','pass2')
  
admin.site.register(mydata3,data)