import django
from django.contrib import admin

from .models import DataAccessLog


@admin.register(DataAccessLog)
class DataAccessLogAdmin(admin.ModelAdmin):
    list_display = ('model', 'viewset', 'user', 'timestamp')
    list_display_links = ('model', 'viewset', 'timestamp')

    fields = ('model', 'viewset', 'timestamp', 'user', 'url', 'response')
    readonly_fields = fields

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        # Before Django 2.1 there wasn't a has_view_permission, thus we use this.
        if django.VERSION < (2, 1):
            return super(DataAccessLogAdmin, self).has_change_permission(request, obj)
        else:
            return False

    def has_delete_permission(self, request, obj=None):
        return False
