from django.contrib import admin
from index import models


def approve_order(model, request, queryset):
    queryset.update(is_available=True)


def disapprove_order(model, request, queryset):
    queryset.update(is_available=False)


class AreaAdmin(admin.ModelAdmin):
    list_display = ('site', 'chance', 'is_secure', 'template_path',)


class VisitorAdmin(admin.ModelAdmin):
    list_display = ('area', 'campaign', 'created_at',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('phone', 'message', 'created_at',)
    actions = (approve_order, disapprove_order)


class ManagerAdmin(admin.ModelAdmin):
    list_display = ('username', 'code',)


class ModeratorAdmin(admin.ModelAdmin):
    list_display = ('username', 'code',)


admin.site.register(models.Area, AreaAdmin)
admin.site.register(models.Visitor, VisitorAdmin)
admin.site.register(models.Campaign)
admin.site.register(models.Partner)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.Manager, ManagerAdmin)
admin.site.register(models.Moderator, ModeratorAdmin)
