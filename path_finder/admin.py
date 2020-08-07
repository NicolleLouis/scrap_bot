from django.contrib import admin
import django.contrib.auth.models
from django.contrib import auth

from path_finder.models.url_data import UrlData, UrlDataAdmin

admin.site.register(UrlData, UrlDataAdmin)

admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)
