from django.contrib import admin
from .models import Admin, Users, Avatar

# Register your models here.
admin.site.register(Admin)

admin.site.register(Users)

admin.site.register(Avatar)