from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "phone", "message", "contact_date")
    list_display_links = ("id", "name")
    search_fields = ("name", "email")
    list_per_page = 20


admin.site.register(Contact, ContactAdmin)
