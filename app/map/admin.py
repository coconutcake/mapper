from django.contrib import admin
from . import models
from django.utils.translation import gettext_lazy as _


# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
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

admin.site.register(models.Department,DepartmentAdmin)

class MapAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['name', 'description','department_fk','floor','id']
    fieldsets = (

        (_('Name'),{'fields': 
            ('name',)}),
        (_('Description'),{"fields": 
            ('description','floor',)}),
        (_('Relations'),{"fields": 
            ('department_fk',)})
    )
    add_fieldsets = (
        (None,{
            'classes': ('wide',),
            'fields': ('name','description')
        }),
    ) 

admin.site.register(models.Map,MapAdmin)