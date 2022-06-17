from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Profile
# Register your models here.



admin.site.site_header = "The Developer Kommunity Administration Panel"
admin.site.unregister(Group)
admin.site.register(Profile)