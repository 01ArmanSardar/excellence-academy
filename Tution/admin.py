from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Tution)


class ApplicationAdmin(admin.ModelAdmin):
    list_display=['user','tution','is_approved','applied_at']
    list_filter=['is_approved']

admin.site.register(models.Application,ApplicationAdmin)
