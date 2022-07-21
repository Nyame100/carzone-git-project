from django.contrib import admin

from pages.models import Team
from django.utils.html import format_html

# Register your models here.


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width=30 style="border-radius: 50px;" />'.format(object.photo.url))

    thumbnail.short_description = 'image'

    list_display = ['first_name', 'thumbnail', 'last_name',
                    'designation', 'photo', 'date_created']
    list_display_links = ['first_name', 'thumbnail', 'last_name']
    search_fields = ['first_name', 'last_name']
    list_filter = ['designation']
