from django.contrib import admin

# Register your models here.
from .models import TwitterUser, Track

admin.site.register(TwitterUser)
admin.site.register(Track)


