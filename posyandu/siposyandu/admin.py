from django.contrib import admin
from siposyandu.models import *

# Register your models here.
class SiposyanduAdmin(admin.ModelAdmin):
     list_display = ['nik','nama','tmpt_lahir','jk','bb','tb','nama_ayah','nama_ibu','agama']
     list_filter = ('nik','nama','jk','agama')
     search_fields = ['nik','nama','jk','agama']
     list_per_page = 100

admin.site.register(Siposyandu, SiposyanduAdmin)

