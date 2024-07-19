from django.contrib import admin
from .models import Refbook, RefbookVersion, RefbookElement

class RefbookElementInline(admin.TabularInline):
    model = RefbookElement
    extra = 1  # Количество пустых форм для нового элемента

class RefbookVersionInline(admin.TabularInline):
    model = RefbookVersion
    extra = 1  # Количество пустых форм для новой версии
    inlines = [RefbookElementInline]

class RefbookAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'get_current_version', 'get_start_date')
    search_fields = ('code', 'name')
    inlines = [RefbookVersionInline]

    def get_current_version(self, obj):
        latest_version = obj.versions.order_by('-start_date').first()
        return latest_version.version if latest_version else '-'

    get_current_version.short_description = 'Текущая версия'

    def get_start_date(self, obj):
        latest_version = obj.versions.order_by('-start_date').first()
        return latest_version.start_date if latest_version else '-'

    get_start_date.short_description = 'Дата начала действия версии'

class RefbookVersionAdmin(admin.ModelAdmin):
    list_display = ('refbook', 'version', 'start_date')
    search_fields = ('refbook__code', 'refbook__name', 'version')
    inlines = [RefbookElementInline]

class RefbookElementAdmin(admin.ModelAdmin):
    list_display = ('get_refbook', 'code', 'value')
    search_fields = ('refbook_version__refbook__code', 'refbook_version__version', 'code', 'value')

    def get_refbook(self, obj):
        return obj.refbook_version.refbook

    get_refbook.short_description = 'Справочник'

admin.site.register(Refbook, RefbookAdmin)
admin.site.register(RefbookVersion, RefbookVersionAdmin)
admin.site.register(RefbookElement, RefbookElementAdmin)
