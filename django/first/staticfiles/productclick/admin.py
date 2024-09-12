from django.contrib import admin
from productclick.models import productclickscount
# Register your models here.


class click(admin.ModelAdmin):
    list_display=('uid','pid','pname','productclick')

admin.site.register(productclickscount,click)