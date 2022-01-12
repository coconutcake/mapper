from django.contrib import admin

# Register your models here.
from . import models
from django.utils.translation import gettext_lazy as _


class ItemAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['name', 'description','location_fk','id']
    fieldsets = (
        (_('Name'),{'fields': 
            ('name',)}),
        (_('Description'),{"fields": 
            ('description',)}),
        (_('Relations'),{"fields": 
            ('location_fk',)}
        )
    )
    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields': ('name','description')
        }),
    ) 

admin.site.register(models.Item,ItemAdmin)