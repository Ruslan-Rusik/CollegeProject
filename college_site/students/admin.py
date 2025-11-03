from django.contrib import admin
from .models import Student, Profile, Group, Club
# Register your models here.

admin.site.register(Student)
admin.site.register(Profile)
admin.site.register(Group)
admin.site.register(Club)