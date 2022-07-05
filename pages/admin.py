from django.contrib import admin

from pages.models import Team

# Register your models here.


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',
                    'designation', 'photo', 'date_created']
