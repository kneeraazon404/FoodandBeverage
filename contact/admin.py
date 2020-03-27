from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    post_display = ("id", "name", "post", "email", "contact_date")
    post_display_links = ("id", "name")
    search_fields = ("name", "email", "post")
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)
