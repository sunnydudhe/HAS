from django.contrib import admin
from . models import *

class doc(admin.ModelAdmin):
    list_display=('id','name','number','specialization')
admin.site.register(Doctor,doc)


class moc(admin.ModelAdmin):
    list_display=('id','name','number','gender','address')
admin.site.register(Patient,moc)


class oc(admin.ModelAdmin):
    list_display=('id','doctor','patient','date','time')
admin.site.register(Appointment,oc)
