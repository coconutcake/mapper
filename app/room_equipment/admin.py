from django.contrib import admin
from . import models
from django.utils.translation import gettext_lazy as _


class ContainerAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['name', 'description','container_type_fk','id']
    fieldsets = (
        (_('Name'),{'fields': 
            ('name',)}),
        (_('Description'),{"fields": 
            ('description',)}),
        (_('Relations'),{"fields": 
            ('container_type_fk',)}
        )
    )
    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields': ('name','description')
        }),
    ) 

admin.site.register(models.Container,ContainerAdmin)


class ContainerTypeAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['name', 'description','id']
    fieldsets = (
        (_('Name'),{'fields': 
            ('name',)}),
        (_('Description'),{"fields": 
            ('description',)}
        )
    )
    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields': ('name','description')
        }),
    ) 

admin.site.register(models.ContainerType,ContainerTypeAdmin)


class ContainerLevelAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['name', 'description','container_fk','id']
    fieldsets = (
        (_('Name'),{'fields': 
            ('name',)}),
        (_('Description'),{"fields": 
            ('description',)}),
        (_('Relations'),{"fields": 
            ('container_fk',)}
        )
    )
    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields': ('name','description')
        }),
    ) 

admin.site.register(models.ContainerLevel,ContainerLevelAdmin)

class LocationAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['name', 'description','container_level_fk', 'location_type','id']
    fieldsets = (
        (_('Name'),{'fields': 
            ('name',)}),
        (_('Description'),{"fields": 
            ('description',)}),
        (_('Relations'),{"fields": 
            ('container_level_fk', 'location_type')}
        )
    )
    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields': ('name','description')
        }),
    ) 

admin.site.register(models.Location,LocationAdmin)

class LocationTypeAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['name', 'description','id']
    fieldsets = (
        (_('Name'),{'fields': 
            ('name',)}),
        (_('Description'),{"fields": 
            ('description',)}
        )
    )
    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields': ('name','description')
        }),
    ) 

admin.site.register(models.LocationType,LocationTypeAdmin)