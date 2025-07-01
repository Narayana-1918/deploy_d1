from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display=['username','password','phone_no']
    