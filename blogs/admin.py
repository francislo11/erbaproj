from django.contrib import admin

# Register your models here.
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'sub_title', 'is_published', 'list_date')
    list_display_link = ('id', 'title', 'sub_title')
    list_editable = ('is_published',)
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
