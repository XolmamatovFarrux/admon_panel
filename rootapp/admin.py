from django.contrib import admin

from .models import *


class KursAdmin(admin.ModelAdmin):
    list_display = ('id','title','start_time','end_time','description')
    list_display_links = ['id','title','description']
    search_fields = ['id    ','title']
    list_filter = ['created_at','updated_at']


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email','kurs')
    list_display_links = ['id','first_name','last_name','email','kurs']
    search_fields = ['id','first_name','last_name']
    list_filter = ['created_at','updated_at']


admin.site.register(Kurs,KursAdmin),
admin.site.register(Student,StudentAdmin),
