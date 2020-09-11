from django.db import models
from django.contrib import admin


class Link(models.Model):
    id = models.IntegerField(
        primary_key=True,
        default=1
    )
    url = models.TextField(
        blank=True,
        null=True
    )
    recursive_occurrence = models.IntegerField(
        default=0
    )
    non_recursive_occurrence = models.IntegerField(
        default=0
    )


class LinkAdmin(admin.ModelAdmin):
    list_display = (
        "url",
        "recursive_occurrence",
        "non_recursive_occurrence"
    )
