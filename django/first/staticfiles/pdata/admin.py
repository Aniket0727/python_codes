from django.contrib import admin
from pdata.models import pdata2
# Register your models here.

class productdata(admin.ModelAdmin):
    list_display=('oname','pname','page','op','sp','pd','address','image','uid','pid')

admin.site.register(pdata2,productdata)