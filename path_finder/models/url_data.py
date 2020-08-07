from django.db import models
from django.contrib import admin


class UrlData(models.Model):
    id = models.IntegerField(
        primary_key=True,
        default=1
    )
    url = models.TextField(
        blank=True,
        null=True
    )
    html_content = models.TextField(
        blank=True,
        null=True
    )


class UrlDataAdmin(admin.ModelAdmin):
    list_display = ("url", "id")
