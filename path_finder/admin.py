from django.contrib import admin
import django.contrib.auth.models
from django.contrib import auth

from path_finder.models.url_data import UrlData, UrlDataAdmin
from path_finder.models.link import Link, LinkAdmin

admin.site.register(UrlData, UrlDataAdmin)
admin.site.register(Link, LinkAdmin)

admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)
