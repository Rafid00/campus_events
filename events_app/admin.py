from django.contrib import admin
from .models import Category, Event


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "start_datetime",
                    "is_approved", "approved_at")
    list_filter = ("is_approved", "category")
    search_fields = ("title", "location", "contact_name", "contact_email")
    list_editable = ("is_approved",)
    readonly_fields = ("created_at", "approved_at")
