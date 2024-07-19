from django.contrib import admin
from .models import Refbook, RefbookVersion, RefbookElement

class RefbookAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'description')
    search_fields = ('code', 'name')

class RefbookVersionAdmin(admin.ModelAdmin):
    list_display = ('refbook', 'version', 'start_date')
    search_fields = ('refbook__name', 'version')

class RefbookElementAdmin(admin.ModelAdmin):
    list_display = ('refbook_version', 'code', 'value')
    search_fields = ('refbook_version__refbook__name', 'code', 'value')

admin.site.register(Refbook, RefbookAdmin)
admin.site.register(RefbookVersion, RefbookVersionAdmin)
admin.site.register(RefbookElement, RefbookElementAdmin)
