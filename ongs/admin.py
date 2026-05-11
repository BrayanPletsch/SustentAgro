from django.contrib import admin

from ongs.models import Ongs


# Register your models here.
@admin.register(Ongs)
class OngsAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name')
    search_fields = ('name', 'short_name')
    ordering = ('name',)

